import mysql.connector
import logging
from datetime import datetime
from pymodbus.client.sync import ModbusTcpClient
import time
import serial
import serial.tools.list_ports
import threading
import pandas as pd

import tkinter as tk
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import font as tkFont
import numpy as np


arduinos={'Latitude': '-12.063190', 'Longitude': '-77.112600', 'Velocity': '0', 'DateTime': '2000-01-01 12:00:00', 'Analog0': '0', 'Analog1': '0', 'Analog2': '0', 'Analog3': '0', 'Analog4': '0', 'Analog5': '0'}
df = pd.DataFrame({'ID':[], 'FECHA_HORA': [], 'ID_ESTACION': [],'ESTACION': [], 'ID_TANQUE':[],'TANQUE':[], 'PRODUCTO':[], 'DENSIDAD':[], 'TAG_SENSOR':[],'DESCRIPCION':[],'UM':[], 'RANGO_MIN':[], 'RANGO_MAX':[],'TIPO':[],'DIRECCION':[],'MASCARA':[],'PUERTO':[],'ID_COMM':[],'SERIAL':[],'LINEAR':[], 'LATITUD':[], 'LONGITUD':[],'VELOCIDAD':[],'MEASURE':[]})
analogico=[0,0,0,0,0,0]

class VentanaSenales(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        plt.style.use('dark_background')
        self.frame_graficas = tk.Frame(self, bg="#6E6E6E")
        self._figure_1, self._ax1 = plt.subplots()
        self._figure_1_canvas = FigureCanvasTkAgg(
            self._figure_1, master=self.frame_graficas
            )
        self._figure_2, self._ax2 = plt.subplots()
        self._figure_2_canvas = FigureCanvasTkAgg(
            self._figure_2, master=self.frame_graficas
            )
        self._figure_3, self._ax3 = plt.subplots()
        self._figure_3_canvas = FigureCanvasTkAgg(
            self._figure_3, master=self.frame_graficas
            )
        self.frame_graficas.grid_columnconfigure(0, weight=1, uniform="fig")
        self.frame_graficas.grid_columnconfigure(1, weight=1, uniform="fig")
        self.frame_graficas.grid_columnconfigure(2, weight=1, uniform="fig")
        self._figure_1_canvas.get_tk_widget().grid(
            row=0, column=0, padx=(10, 30), pady=(30, 30),
            sticky="nsew"
            )
        self._figure_2_canvas.get_tk_widget().grid(
            row=0, column=1, padx=(10, 30), pady=(30, 30),
            sticky="nsew"
            )
        self._figure_3_canvas.get_tk_widget().grid(
            row=0, column=2, padx=(10, 30), pady=(30, 30),
            sticky="nsew"
            )
        self.frame_botones = tk.Frame(self, bg="#151515")
        self.btn_iniciar = tk.Button(
            self.frame_botones, bg="#7401DF", fg="#FFBF00",
            activebackground="#8258FA", font=('Courier', 16),
            text="Iniciar", command=self.iniciar_animacion
            )
        self.btn_pausar = tk.Button(
            self.frame_botones, bg="#7401DF", fg="#FFBF00",
            activebackground="#8258FA", font=('Courier', 16),
            text="  Pausa  ", command=self.pausar_animacion, state=tk.DISABLED
            )
        self.btn_iniciar.pack(
            side="left", padx=(100, 100), pady=(100, 100),
            fill="y", expand=True
            )
        self.btn_pausar.pack(
            side="left", padx=(100, 100), pady=(100, 100),
            fill="y", expand=True
            )
        self._anim1 = None
        self._anim2 = None
        self._anim3 = None
        self.frame_graficas.pack(fill="both", expand=True)
        self.frame_botones.pack(fill="x")
        self._init_axes()
    def _init_axes(self):
        self._ax1.set_title('Signal')
        self._ax1.set_xlabel("Time")
        self._ax1.set_ylabel("Amplitude")
        self._ax1.set_xlim(0, 100)
        self._ax1.set_ylim(-1, 1)
        self._ax2.set_title('Signal2')
        self._ax2.set_xlabel("Time")
        self._ax2.set_ylabel("Amplitude")
        self._ax2.set_xlim(0, 100)
        self._ax2.set_ylim(-1, 1)
        self._ax3.set_title('Signal3')
        self._ax3.set_xlabel("Time")
        self._ax3.set_ylabel("Amplitude")
        self._ax3.set_xlim(0, 100)
        self._ax3.set_ylim(-1, 1)


    def iniciar_animacion(self):

        def animate(values):
            value=values
            data.append(value)
            lines.set_data(range(0, 100), data)
            return lines

        def animate2(values):
            value=values
            data2.append(value)
            lines2.set_data(range(0, 100), data2)
            return lines2

        def animate3(values):
            value=values
            data3.append(value)
            lines3.set_data(range(0, 100), data3)
            return lines3

        def data_gen():
            for k in range(100):
                t = k / 100
                yield 0.5 * np.sin(40 * t) * np.exp(-2 * t)

        def data_gen2():
            for k in range(100):
                t = k / 100
                yield 0.5 * np.sin(60 * t)

        def data_gen3():
            for k in range(100):
                t = k / 100
                yield 0.5 * np.cos(60 * t)

        if self._anim1 is None:
            lines = self._ax1.plot([], [], color='#80FF00')[0]
            lines2 = self._ax2.plot([], [], color='#80FF00')[0]
            lines3 = self._ax3.plot([], [], color='#80FF00')[0]

            data = collections.deque([0] * 100, maxlen=100)
            data2 = collections.deque([0] * 100, maxlen=100)
            data3 = collections.deque([0] * 100, maxlen=100)

            self._anim1 = animation.FuncAnimation(
                self._figure_1, animate, data_gen, interval=5
                )
            self._anim2 = animation.FuncAnimation(
                self._figure_2, animate2, data_gen2, interval=5
                )
            self._anim3 = animation.FuncAnimation(
                self._figure_3, animate3, data_gen3, interval=5
                )

            self._figure_1_canvas.draw()
            self._figure_2_canvas.draw()
            self._figure_3_canvas.draw()

            self.btn_pausar.configure(state=tk.NORMAL)
            self.btn_iniciar.configure(text="Detener")
        else:
            self._ax1.lines = []  
            self._ax2.lines = []
            self._ax3.lines = []
            self.btn_pausar.configure(state=tk.DISABLED, text="  Pausa  ")
            self.btn_iniciar.configure(text="Iniciar")
            self._anim1 = self._anim2 = self._anim3 = None


    def pausar_animacion(self):
        if self.btn_pausar["text"] == "  Pausa  ":
            self._anim1.event_source.stop()
            self._anim2.event_source.stop()
            self._anim3.event_source.stop()
            self.btn_pausar.configure(text="Continuar")

        else:
            self._anim1.event_source.start()
            self._anim2.event_source.start()
            self._anim3.event_source.start()
            self.btn_pausar.configure(text="  Pausa  ")



def init_logger():
    FORMAT = ('%(asctime)s - %(threadName)s %(levelname)s %(module)s %(lineno)s %(message)s')
    logging.basicConfig(filename='Roraima_Log.txt', filemode='w',format=FORMAT)
    log=logging.getLogger()
    log.setLevel(logging.DEBUG)

def init_arduino():   
    arduino_ports=[]
    for p in serial.tools.list_ports.comports():
        if 'Arduino' in p.manufacturer:
            arduino_ports = p.device
            logging.info("Info Puerto Serie Arduino:"+str(p.device))
            return arduino_ports,True
    return arduino_ports,False

def Arduino_Comm():
    global arduinos
    global analogico
    while(True):
        arduino_port,F_OK = init_arduino()
        arduino = serial.Serial(arduino_port,9600, timeout=50)
        time.sleep(10)
        if F_OK:
            comando = 'ready'+'\n'
            try:
                a=arduino.write(comando.encode())
                lectura = arduino.readline()
            except:
                logging.error("No se puede contectar a Tarjeta ARDUINO")    
            txt=str(lectura)
            txt=txt[2:-5]
            if txt.find('Latitude')<0  or txt.find('Longitude')<0:
                logging.info("Error de lectura en cadena Serial")
            else:
                SerialA=txt.split("|")
                for S in SerialA:
                    CLAVE=S.split("=")[0]
                    VALOR=S.split("=")[1]
                    if VALOR=="INVALID DATETIME":
                        VALOR=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    if VALOR=="INVALID SPEED":
                        VALOR="0"
                    if VALOR=="INVALID LATITUDE":
                        VALOR=LAST_VALID_LAT
                    if VALOR=="INVALID LONGITUDE":
                        VALOR=LAST_VALID_LON
                    if CLAVE=="Latitude":
                        LAST_VALID_LAT=VALOR
                    if CLAVE=="Longitude":
                        LAST_VALID_LON=VALOR
                    arduinos[CLAVE]=VALOR
            analogico=[0,0,0,0,0,0]
            analogico[0]=int(arduinos["Analog0"])
            analogico[1]=int(arduinos["Analog1"])
            analogico[2]=int(arduinos["Analog2"])
            analogico[3]=int(arduinos["Analog3"])
            analogico[4]=int(arduinos["Analog4"])
            analogico[5]=int(arduinos["Analog5"])
        else:
            logging.error("No se puede contectar a Tarjeta ARDUINO")    

def Read_Conf():
    df=pd.DataFrame=[]
    try:
        connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
        cursor=connection.cursor()
        df=pd.read_sql("SELECT * FROM MAIN_SENSOR.DATA WHERE ID IN (SELECT MAX(ID) FROM MAIN_SENSOR.DATA GROUP BY TAG_SENSOR)", connection)
        return df, True
    except:
        logging.error("No se puede contectar a base de datos Main Sensor de este dispositivo")
        cursor.close()
        connection.close()
        print(df)
        return df,False

def Read_Measure():
    df,F_OK=Read_Conf()
    df['MEASURE']='0'
    df['ID']='0'
    df['LATITUD']=arduinos['Latitude']
    df['LONGITUD']=arduinos['Longitude']
    df['VELOCIDAD']=arduinos['Velocity']
    df['FECHA_HORA']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if F_OK:
        for i in range(len(df)):
            if df['TIPO'].loc[i]=='ModbusTCP':
                client = ModbusTcpClient(df['DIRECCION'].loc[i],port=int(df['PUERTO'].loc[i]))
                if client.connect():
                    CCOM=df['ID_COMM'].loc[i] 
                    CCOM1=CCOM.split(':')
                    ID=int(CCOM1[i])
                    DIRECCION=int(CCOM1[1])-40001
                    try:
                        rr = client.read_holding_registers(DIRECCION,1,unit=ID)
                        Med_lin=linealization(rr.registers[0],df['LINEAR'].iloc[i])
                        df['MEASURE'].loc[i]=str(Med_lin)
                    except:
                        logging.exception("No se puede leer registros: "+ df['TAG_SENSOR'].loc[i])
            if df['TIPO'].loc[i]=="Analogico":
                    canal=int(df['ID_COMM'].loc[i])
                    try:
                        rANA=(float(analogico[canal])-(1024/5))/(1024-(1024/5))
                        rMed=rANA*(float(df['RANGO_MAX'].loc[i])-float(df['RANGO_MIN'].loc[i]))+float(df['RANGO_MIN'].loc[i])
                        Med_lin=linealization(rMed,df['LINEAR'].iloc[i])
                        df['MEASURE'].loc[i]=str(Med_lin)
                        if float(analogico[canal])<(1024/5):
                            logging.warning("Medicion de sensor Analogico por debajo de 1 V: " + df['TAG_SENSOR'].loc[i])
                    except:
                        logging.error("Error en sensor Analogico (112) : " + df['TAG_SENSOR'].loc[i])
    return df

def linealization(var,linear):
    linear1=linear[1:-1].split(',')
    for i in range(len(linear1)):
        xx=linear1[i].split(':')
        xx1=linear1[i+1].split(':')
        print(xx)
        print(xx1)
        try:
            x1=float(xx[0])
            x2=float(xx1[0])
            y1=float(xx[1])
            y2=float(xx1[1])
            if (var>=x1 and var<=x2):
                valor=(var-x1)*((y2-y1)/(x2-x1))+y1
                return valor
        except:
            return 0
    return 0

def database_write(df):
    try:
        connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
        cursor=connection.cursor()
        Query="INSERT INTO MAIN_SENSOR.DATA (`FECHA_HORA`,`ID_ESTACION`,`ESTACION`,`ID_TANQUE`,`TANQUE`,`PRODUCTO`,`DENSIDAD`,`TAG_SENSOR`,`DESCRIPCION`,`UM`, `RANGO_MIN`, `RANGO_MAX`, `TIPO`,`DIRECCION`, `MASCARA`, `PUERTO`,`ID_COMM`,`SERIAL`,`LINEAR`,`LATITUD`,`LONGITUD`,`VELOCIDAD`,`MEASURE`) VALUES (%(FECHA_HORA)s,%(ID_ESTACION)s,%(ESTACION)s,%(ID_TANQUE)s,%(TANQUE)s,%(PRODUCTO)s,%(DENSIDAD)s,%(TAG_SENSOR)s,%(DESCRIPCION)s,%(UM)s, %(RANGO_MIN)s, %(RANGO_MAX)s, %(TIPO)s,%(DIRECCION)s, %(MASCARA)s, %(PUERTO)s,%(ID_COMM)s,%(SERIAL)s,%(LINEAR)s,%(LATITUD)s,%(LONGITUD)s,%(VELOCIDAD)s,%(MEASURE)s)"
        for i in range(len(df)):
            cursor.execute(Query,df.loc[i].to_dict())
        connection.commit()
        cursor.close()
        connection.close()
    except:
        logging.error("Error: Falla al Escribir DB")

def Roraima_Comm():
    while(True):
        df=Read_Measure()
        database_write(df)


#creation of an instance


if __name__ == "__main__":
    init_logger()
    hilo1 = threading.Thread(target=Arduino_Comm)
    hilo2 = threading.Thread(target=Roraima_Comm)
    hilo1.start()
    time.sleep(10)
    hilo2.start()
    root = tk.Tk()
    VentanaSeñales(root).pack(side="top", fill="both", expand=True)
    root.mainloop()