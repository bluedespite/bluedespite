import mysql.connector
import logging
from datetime import datetime
from pymodbus.client.sync import ModbusTcpClient
import time
import serial
import serial.tools.list_ports
import threading
import pandas as pd
arduinos={}
df = pd.DataFrame({'ID': [], 'ID_ESTACION': [],'ESTACION': [], 'ID_TANQUE':[],'TANQUE':[], 'PRODUCTO':[], 'DENSIDAD':[], 'TAG_SENSOR':[],'DESCRIPCION':[],'UM':[], 'RANGO_MIN':[], 'RANGO_MAX':[],'TIPO':[],'DIRECCION':[],'MASCARA':[],'PUERTO':[],'ID_COMM':[],'SERIAL':[],'LINEAR':[]})
analogico=[0,0,0,0,0,0]

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

def Arduino_Comm(arduino_port):
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
        df=pd.read_sql("SELECT * FROM MAIN_SENSOR.CONF", connection)
        return df, True
    except:
        logging.error("No se puede contectar a base de datos Main Sensor de este dispositivo")
        cursor.close()
        connection.close()
        return df,False
def Read_Measure():
    df,F_OK=Read_Conf()
    df['MEASURE']=0
    df['LATITUD']=arduinos['Latitude']
    df['LONGITUD']=arduinos['Longitude']
    df['VELOCIDAD']=arduinos['Velocity']
    df['FECHA_HORA']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if F_OK:
        for i in range(len(df)):
            if df['TIPO'].loc[i]=='ModbusTCP':
                client = ModbusTcpClient(df['DIRECCION'].loc[i],port=int(df['PUERTO'].loc[i]))
                if client.connect():
                    CCOM=df['ID'].loc[0] 
                    CCOM1=CCOM.split(':')
                    ID=int(CCOM1[0])
                    DIRECCION=int(CCOM1[1])-40001
                    try:
                        rr = client.read_holding_registers(DIRECCION,1,unit=ID)
                        df['MEASURE'].loc[i]=rr.registers[0]
                    except:
                        logging.exception("No se puede leer registros: "+ df['TAG_SENSOR'].loc[i])
            if df['TIPO'].loc[i]=="Analogico":
                    canal=int(df['ID'].loc[i])
                    try:
                        rANA=(float(analogico[canal])-(1024/5))/(1024-(1024/5))
                        rMed=rANA*(float(df['RANGO_MAX'].loc[i])-float(df['RANGO_MIN'].loc[i]))+float(df['RANGO_MIN'].loc[i])
                        df['MEASURE'].loc[i]=rMed
                        if float(analogico[canal])<(1024/5):
                            logging.warning("Medicion de sensor Analogico por debajo de 1 V: " + df['TAG_SENSOR'].loc[i])
                    except:
                        logging.error("Error en sensor Analogico (113) : " + df['TAG_SENSOR'].loc[i])
    return df
def Roraima_Comm():
    df =pd.DataFrame()
    result=Read_Measure({'ID': [],ID': [] })



def contar():
    contador = 0
    while contador<100:
        contador+=1
        #print('Hilo:', threading.current_thread().getName(), 'con identificador:',  threading.current_thread().ident,'Contador:', contador)

init_logger()
hilo1 = threading.Thread(target=Arduino_Comm)
hilo2 = threading.Thread(target=contar)
hilo1.start()
hilo2.start()


fecha=arduinos["DateTime"]
        