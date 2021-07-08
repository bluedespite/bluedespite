from tkinter import *
from typing import ValuesView
import mysql.connector
from tkinter import messagebox as MessageBox
from tkinter import ttk, font
import pandas as pd
from datetime import datetime

df = pd.DataFrame({'ID':[], 'FECHA_HORA': [], 'ID_ESTACION': [],'ESTACION': [], 'ID_TANQUE':[],'TANQUE':[], 'PRODUCTO':[], 'DENSIDAD':[], 'TAG_SENSOR':[],'DESCRIPCION':[],'UM':[], 'RANGO_MIN':[], 'RANGO_MAX':[],'TIPO':[],'DIRECCION':[],'MASCARA':[],'PUERTO':[],'ID_COMM':[],'SERIAL':[],'LINEAR':[], 'LATITUD':[], 'LONGITUD':[],'VELOCIDAD':[]})

class Window:
    def __init__(self):
        indice=-1
        self.ventana=Tk()
        self.ventana.geometry("800x400")
        self.ventana.title("Roraima: Configuracion Inicial")
        menubar = Menu(self.ventana)
        self.ventana.config(menu=menubar)
        Archivo = Menu(menubar, tearoff=0)
        Ayuda = Menu(menubar, tearoff=0)
        Archivo.add_command(label="Nuevo")
        Archivo.add_command(label="Editar")
        Archivo.add_command(label="Exit", command=self.client_exit)
        menubar.add_cascade(label="Archivo", menu=Archivo)
        Ayuda.add_command(label="Acerca de..", command=self.acerca_de)
        menubar.add_cascade(label="Ayuda", menu=Ayuda)
        img = PhotoImage(file="Roraima2.gif")
        lab=Label(image=img).place(x=0,y=0)
        test=Button(text ="TEST DB", command = self.database_connect)
        test.grid(column=1,row=13)
        Init=Button(text ="INIT DB", command = self.database_init)
        Init.grid(column=2,row=13)
        Read=Button(text ="READ DB", command = self.database_read)
        Read.grid(column=3,row=13)
        Write=Button(text ="WRITE DB", command = self.database_write)
        Write.grid(column=4,row=13)
        Ultimo=Button(text ="APPEND", command = self.ultimo)
        Ultimo.grid(column=1,row=12)
        Buscar=Button(text ="SEARCH ID", command = self.Search_ID)
        Buscar.grid(column=2,row=12)
        StartOver=Button(text ="Start Over", command = self.StartOver)
        StartOver.grid(column=3,row=12)
        #ID de la Estacion
        self.ventana.etiq1=Label(self.ventana, text="ID Estacion: $ID_ESTACION")
        self.ventana.etiq1.grid(column=1,row=0,sticky="E")
        self.ventana.centr1=Entry(self.ventana, width=20)
        self.ventana.centr1.grid(column=2,row=0)
        #Nombre de la Estacion
        self.ventana.etiq2=Label(self.ventana, text="Nombre Estacion: $ESTACION")
        self.ventana.etiq2.grid(column=1,row=1,sticky="E")
        self.ventana.centr2=Entry(self.ventana, width=20)
        self.ventana.centr2.grid(column=2,row=1)
        #ID del Tanque
        self.ventana.etiq3=Label(self.ventana, text="ID Tanque: $ID_TANQUE")
        self.ventana.etiq3.grid(column=1,row=2,sticky="E")
        self.ventana.centr3=Entry(self.ventana, width=20)
        self.ventana.centr3.grid(column=2,row=2)
        #Nombre del Tanque
        self.ventana.etiq4=Label(self.ventana, text="Nombre Tanque: $TANQUE")
        self.ventana.etiq4.grid(column=1,row=3,sticky="E")
        self.ventana.centr4=Entry(self.ventana, width=20)
        self.ventana.centr4.grid(column=2,row=3)
        #Producto Almacenado
        self.ventana.etiq5=Label(self.ventana, text="Producto Tk: $PRODUCTO")
        self.ventana.etiq5.grid(column=1,row=4,sticky="E")
        self.ventana.centr5=Entry(self.ventana, width=20)
        self.ventana.centr5.grid(column=2,row=4)
        #Densidad del Producto (Kgr/cm2)
        self.ventana.etiq6=Label(self.ventana, text="Densidad(Kgr/cm2): $DENSIDAD")
        self.ventana.etiq6.grid(column=1,row=5,sticky="E")
        self.ventana.centr6=Entry(self.ventana, width=20)
        self.ventana.centr6.grid(column=2,row=5)
        #Tag del Instrumento
        self.ventana.etiq7=Label(self.ventana, text="Tag Instrumento: $TAG_SENSOR")
        self.ventana.etiq7.grid(column=1,row=6,sticky="E")
        self.ventana.centr7=Entry(self.ventana, width=20)
        self.ventana.centr7.grid(column=2,row=6)
        #Descripcion Instrumento
        self.ventana.etiq8=Label(self.ventana, text="Descripcion: $DESCRIPCION")
        self.ventana.etiq8.grid(column=1,row=7,sticky="E")
        self.ventana.centr8=Entry(self.ventana, width=20)
        self.ventana.centr8.grid(column=2,row=7)
        #Unidad de la Medida
        self.ventana.etiq9=Label(self.ventana, text="Unidad Medida: $UM")
        self.ventana.etiq9.grid(column=1,row=8,sticky="E")
        self.ventana.centr9=Entry(self.ventana, width=20)
        self.ventana.centr9.grid(column=2,row=8)
        #Rango Minimo
        self.ventana.etiq10=Label(self.ventana, text="Rango Minimo: $RANGO_MIN")
        self.ventana.etiq10.grid(column=1,row=9,sticky="E")
        self.ventana.centr10=Entry(self.ventana, width=20)
        self.ventana.centr10.grid(column=2,row=9)
        #Rango Maximo
        self.ventana.etiq11=Label(self.ventana, text="Rango Maximo: $RANGO_MAX")
        self.ventana.etiq11.grid(column=1,row=10,sticky="E")
        self.ventana.centr11=Entry(self.ventana, width=20)
        self.ventana.centr11.grid(column=2,row=10)
        #Tipo de Entrada
        self.ventana.etiq12=Label(self.ventana, text="Tipo de Entrada: $TIPO")
        self.ventana.etiq12.grid(column=3,row=0,sticky="E")
        self.ventana.centr12=ttk.Combobox(self.ventana, width=20,values=["Analogico","ModbusTCP","Modbus RS232"])
        self.ventana.centr12.grid(column=4,row=0)
        #Direccion del instrumento
        self.ventana.etiq13=Label(self.ventana, text="Dir Instrumento: $DIRECCION")
        self.ventana.etiq13.grid(column=3,row=1,sticky="E")
        self.ventana.centr13=Entry(self.ventana, width=20)
        self.ventana.centr13.grid(column=4,row=1)
        self.ventana.centr13.insert(0,"192.168.1.25")
        #Mascara de Subred
        self.ventana.etiq14=Label(self.ventana, text="Mascara de Subred: $MASCARA")
        self.ventana.etiq14.grid(column=3,row=2,sticky="E")
        self.ventana.centr14=Entry(self.ventana, width=20)
        self.ventana.centr14.grid(column=4,row=2)
        self.ventana.centr14.insert(0,"255.255.255.0")
        #Puerto de Comunicaiones
        self.ventana.etiq15=Label(self.ventana, text="Puerto de Comm: $PUERTO")
        self.ventana.etiq15.grid(column=3,row=3,sticky="E")
        self.ventana.centr15=Entry(self.ventana, width=20)
        self.ventana.centr15.grid(column=4,row=3)
        self.ventana.centr15.insert(0,"502")
        #ID de comunicacion
        self.ventana.etiq16=Label(self.ventana, text="ID de Comm:Regist: $ID")
        self.ventana.etiq16.grid(column=3,row=4,sticky="E")
        self.ventana.centr16=Entry(self.ventana, width=20)
        self.ventana.centr16.grid(column=4,row=4)
        self.ventana.centr16.insert(0,"1:400020")
        #Serial Settings
        self.ventana.etiq17=Label(self.ventana, text="Serial Settings: $SERIAL")
        self.ventana.etiq17.grid(column=3,row=5,sticky="E")
        self.ventana.centr17=Entry(self.ventana, width=20)
        self.ventana.centr17.grid(column=4,row=5)
        self.ventana.centr17.insert(0,"9600;N;8;1")
        #Tabla de Linealizacion
        self.ventana.etiq18=Label(self.ventana, text="Tabla Linealizac[(X:Y)] $LINEAR")
        self.ventana.etiq18.grid(column=3,row=6,sticky="E")
        self.ventana.centr18=Entry(self.ventana, width=20)
        self.ventana.centr18.insert(0,"[0:0,25:25,50:50,75:75,100:100]")
        self.ventana.centr18.grid(column=4,row=6)
        self.ventana.mainloop()
    def client_exit(self):
        exit()
    def StartOver(self):
        df = pd.DataFrame({'ID':[], 'FECHA_HORA': [], 'ID_ESTACION': [],'ESTACION': [], 'ID_TANQUE':[],'TANQUE':[], 'PRODUCTO':[], 'DENSIDAD':[], 'TAG_SENSOR':[],'DESCRIPCION':[],'UM':[], 'RANGO_MIN':[], 'RANGO_MAX':[],'TIPO':[],'DIRECCION':[],'MASCARA':[],'PUERTO':[],'ID_COMM':[],'SERIAL':[],'LINEAR':[], 'VELOCIDAD':[], 'LATITUD':[],'LONGITUD':[]})
    def ultimo(self):
        global df
        df.loc[len(df)]=[str(0),datetime.now().strftime('%Y-%m-%d %H:%M:%S'),self.ventana.centr1.get(),self.ventana.centr2.get(),self.ventana.centr3.get(),self.ventana.centr4.get(),self.ventana.centr5.get(),self.ventana.centr6.get(),self.ventana.centr7.get(),self.ventana.centr8.get(),self.ventana.centr9.get(),self.ventana.centr10.get(),self.ventana.centr11.get(),self.ventana.centr12.get(),self.ventana.centr13.get(),self.ventana.centr14.get(),self.ventana.centr15.get(),self.ventana.centr16.get(),self.ventana.centr17.get(),self.ventana.centr18.get(),'0','-12.063190','-77.112600']
        print(df)
    def acerca_de(self):
        MessageBox.showinfo("Acerca de..", " Proyecto Roraima \n Jul-2021 \n Miguel Angel Aguirre")
    def database_connect(self):
        try:
            connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
            cursor=connection.cursor()
            MessageBox.showinfo("Success", "TEST:Conexion Exitosa")
            connection.close()
        except:
            MessageBox.showerror("Error", "TEST:Fallo de Conexion")
    def database_init(self):
        try:
            connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
            cursor=connection.cursor()
            Query= "CREATE OR REPLACE TABLE MAIN_SENSOR.DATA ( `ID` INT NOT NULL PRIMARY KEY AUTO_INCREMENT , `FECHA_HORA` DATETIME NOT NULL,`ID_ESTACION` TEXT NOT NULL ,`ESTACION` TEXT NOT NULL,`ID_TANQUE` TEXT NOT NULL,`TANQUE` TEXT NOT NULL,`PRODUCTO` TEXT NOT NULL,`DENSIDAD` TEXT NOT NULL,`TAG_SENSOR` TEXT NOT NULL,`DESCRIPCION` TEXT NOT NULL,`UM` TEXT NOT NULL, `RANGO_MIN` FLOAT NOT NULL, `RANGO_MAX` FLOAT NOT NULL, `TIPO` TEXT NOT NULL,`DIRECCION` TEXT NOT NULL, `MASCARA` TEXT NOT NULL, `PUERTO` TEXT NOT NULL,`ID_COMM` TEXT NOT NULL,`SERIAL` TEXT NOT NULL,`LINEAR` TEXT NOT NULL,`VELOCIDAD` FLOAT NOT NULL, `LATITUD` FLOAT NOT NULL,`LONGITUD` FLOAT NOT NULL)"
            cursor.execute(Query)
            MessageBox.showinfo("Success", "Inicializacion Exitosa DB")
            cursor.close()
            connection.close()
        except:
            MessageBox.showerror("Error", "Fallo de Inicializacion DB")
    def database_write(self):
        global df
        try:
            connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
            cursor=connection.cursor()
            Query="INSERT INTO MAIN_SENSOR.DATA (`FECHA_HORA`,`ID_ESTACION`,`ESTACION`,`ID_TANQUE`,`TANQUE`,`PRODUCTO`,`DENSIDAD`,`TAG_SENSOR`,`DESCRIPCION`,`UM`, `RANGO_MIN`, `RANGO_MAX`, `TIPO`,`DIRECCION`, `MASCARA`, `PUERTO`,`ID_COMM`,`SERIAL`,`LINEAR`,`VELOCIDAD`,`LATITUD`,`LONGITUD`) VALUES (%(FECHA_HORA)s,%(ID_ESTACION)s,%(ESTACION)s,%(ID_TANQUE)s,%(TANQUE)s,%(PRODUCTO)s,%(DENSIDAD)s,%(TAG_SENSOR)s,%(DESCRIPCION)s,%(UM)s, %(RANGO_MIN)s, %(RANGO_MAX)s, %(TIPO)s,%(DIRECCION)s, %(MASCARA)s, %(PUERTO)s,%(ID_COMM)s,%(SERIAL)s,%(LINEAR)s,%(VELOCIDAD)s,%(LATITUD)s,%(LONGITUD)s)"
            for i in range(len(df)):
                if df['ID'].loc[i]=='0':
                    cursor.execute(Query,df.loc[i].to_dict())
            connection.commit()
            MessageBox.showinfo("Success", "Escritura Exitosa en DB")
        except:
            MessageBox.showerror("Error", "Falla al Escribir DB")
        connection.close()
    def database_read(self):
        global df
        try:
            connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
            cursor=connection.cursor()
            df=pd.read_sql("SELECT * FROM MAIN_SENSOR.DATA WHERE ID IN (SELECT MAX(ID) FROM MAIN_SENSOR.DATA GROUP BY TAG_SENSOR)", connection)
            MessageBox.showinfo("Success", "Se leyeron "+str(len(df))+ " Registros")
            cursor.close()
            connection.close()
        except:
            MessageBox.showerror("Error", "Falló al Leer DB")
    def Search_ID(self):
        indice=df[df['TAG_SENSOR']==self.ventana.centr7.get()].last_valid_index()
        self.ventana.centr1.delete(0,END)
        self.ventana.centr2.delete(0,END)
        self.ventana.centr3.delete(0,END)
        self.ventana.centr4.delete(0,END)
        self.ventana.centr5.delete(0,END)
        self.ventana.centr6.delete(0,END)
        self.ventana.centr7.delete(0,END)
        self.ventana.centr8.delete(0,END)
        self.ventana.centr9.delete(0,END)
        self.ventana.centr10.delete(0,END)
        self.ventana.centr11.delete(0,END)
        self.ventana.centr12.delete(0,END)
        self.ventana.centr13.delete(0,END)
        self.ventana.centr14.delete(0,END)
        self.ventana.centr15.delete(0,END)
        self.ventana.centr16.delete(0,END)
        self.ventana.centr17.delete(0,END)
        self.ventana.centr18.delete(0,END)
        try:
            self.ventana.centr1.insert(0,df['ID_ESTACION'].iloc[indice])
            self.ventana.centr2.insert(0,df['ESTACION'].iloc[indice])
            self.ventana.centr3.insert(0,df['ID_TANQUE'].iloc[indice])
            self.ventana.centr4.insert(0,df['TANQUE'].iloc[indice])
            self.ventana.centr5.insert(0,df['PRODUCTO'].iloc[indice])
            self.ventana.centr6.insert(0,df['DENSIDAD'].iloc[indice])
            self.ventana.centr7.insert(0,df['TAG_SENSOR'].iloc[indice])
            self.ventana.centr8.insert(0,df['DESCRIPCION'].iloc[indice])
            self.ventana.centr9.insert(0,df['UM'].iloc[indice])
            self.ventana.centr10.insert(0,df['RANGO_MIN'].iloc[indice])
            self.ventana.centr11.insert(0,df['RANGO_MAX'].iloc[indice])
            self.ventana.centr12.insert(0,df['TIPO'].iloc[indice])
            self.ventana.centr13.insert(0,df['DIRECCION'].iloc[indice])
            self.ventana.centr14.insert(0,df['MASCARA'].iloc[indice])
            self.ventana.centr15.insert(0,df['PUERTO'].iloc[indice])
            self.ventana.centr16.insert(0,df['ID_COMM'].iloc[indice])
            self.ventana.centr17.insert(0,df['SERIAL'].iloc[indice])
            self.ventana.centr18.insert(0,df['LINEAR'].iloc[indice])
        except:
            MessageBox.showerror("Error", "Out of Bounds")
#creation of an instance
app = Window()
