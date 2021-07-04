from tkinter import *
from typing import ValuesView
import mysql.connector
from tkinter import messagebox as MessageBox
from tkinter import ttk, font
import pandas as pd
from PIL import ImageTk,Image

df = pd.DataFrame({'ID': [], 'ID_ESTACION': [],'ESTACION': [], 'ID_TANQUE':[],'TANQUE':[], 'PRODUCTO':[], 'DENSIDAD':[], 'TAG_SENSOR':[],'DESCRIPCION':[],'UM':[], 'RANGO_MIN':[], 'RANGO_MAX':[],'TIPO':[],'DIRECCION':[],'MASCARA':[],'PUERTO':[],'ID_COMM':[],'LINEAR':[]})
columnas=list(df.keys())
class Window:
    def __init__(self):
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
        img = Image.open("Roraima.jpg")
        img = img.resize((800,400),Image.ANTIALIAS)
        photog = ImageTk.PhotoImage(img)
        lab=Label(image=photog).place(x=0,y=0)
        #Numero de Entrada (ID)
        self.ventana.etiq0=Label(self.ventana, text="Numero de Entrada: $"+columnas[0])
        self.ventana.etiq0.grid(column=1,row=0,sticky="E")
        self.ventana.centr0=Entry(self.ventana, width=30)
        self.ventana.centr0.grid(column=2,row=0)
        #ID de la Estacion
        self.ventana.etiq1=Label(self.ventana, text="ID de la Estacion: $"+columnas[1])
        self.ventana.etiq1.grid(column=1,row=1,sticky="E")
        self.ventana.centr1=Entry(self.ventana, width=30)
        self.ventana.centr1.grid(column=2,row=1)
        #Nombre de la Estacion
        self.ventana.etiq2=Label(self.ventana, text="Nombre de la Estacion: $"+columnas[2])
        self.ventana.etiq2.grid(column=1,row=2,sticky="E")
        self.ventana.centr2=Entry(self.ventana, width=30)
        self.ventana.centr2.grid(column=2,row=2)
        #ID del Tanque
        self.ventana.etiq3=Label(self.ventana, text="ID del Tanque: $"+columnas[3])
        self.ventana.etiq3.grid(column=1,row=3,sticky="E")
        self.ventana.centr3=Entry(self.ventana, width=30)
        self.ventana.centr3.grid(column=2,row=3)
        #Nombre del Tanque
        self.ventana.etiq4=Label(self.ventana, text="Nombre del Tanque: $"+columnas[4])
        self.ventana.etiq4.grid(column=1,row=4,sticky="E")
        self.ventana.centr4=Entry(self.ventana, width=30)
        self.ventana.centr4.grid(column=2,row=4)
        #Producto Almacenado
        self.ventana.etiq5=Label(self.ventana, text="Producto Almacenado: $"+columnas[5])
        self.ventana.etiq5.grid(column=1,row=5,sticky="E")
        self.ventana.centr5=Entry(self.ventana, width=30)
        self.ventana.centr5.grid(column=2,row=5)
        #Densidad del Producto (Kgr/cm2)
        self.ventana.etiq6=Label(self.ventana, text="Densidad Producto (Kgr/cm2): $"+columnas[6])
        self.ventana.etiq6.grid(column=1,row=6,sticky="E")
        self.ventana.centr6=Entry(self.ventana, width=30)
        self.ventana.centr6.grid(column=2,row=6)
        #Tag del Instrumento
        self.ventana.etiq7=Label(self.ventana, text="Tag del Instrumento: $"+columnas[7])
        self.ventana.etiq7.grid(column=1,row=7,sticky="E")
        self.ventana.centr7=Entry(self.ventana, width=30)
        self.ventana.centr7.grid(column=2,row=7)
        #Descripcion Instrumento
        self.ventana.etiq8=Label(self.ventana, text="Descripcion Instrumento: $"+columnas[8])
        self.ventana.etiq8.grid(column=1,row=8,sticky="E")
        self.ventana.centr8=Entry(self.ventana, width=30)
        self.ventana.centr8.grid(column=2,row=8)
        #Unidad de la Medida
        self.ventana.etiq9=Label(self.ventana, text="Unidad de la Medida: $"+columnas[9])
        self.ventana.etiq9.grid(column=1,row=9,sticky="E")
        self.ventana.centr9=Entry(self.ventana, width=30)
        self.ventana.centr9.grid(column=2,row=9)
        #Rango Minimo
        self.ventana.etiq10=Label(self.ventana, text="Rango Minimo: $"+columnas[10])
        self.ventana.etiq10.grid(column=1,row=10,sticky="E")
        self.ventana.centr10=Entry(self.ventana, width=30)
        self.ventana.centr10.grid(column=2,row=10)
        #Rango Maximo
        self.ventana.etiq11=Label(self.ventana, text="Rango Maximo: $"+columnas[11])
        self.ventana.etiq11.grid(column=1,row=11,sticky="E")
        self.ventana.centr11=Entry(self.ventana, width=30)
        self.ventana.centr11.grid(column=2,row=11)
        #Tipo de Entrada
        self.ventana.etiq12=Label(self.ventana, text="Tipo de Entrada: $"+columnas[12])
        self.ventana.etiq12.grid(column=1,row=12,sticky="E")
        self.ventana.centr12=ttk.Combobox(self.ventana, width=28,values=["Analogico","ModbusTCP","Modbus RS232"])
        self.ventana.centr12.grid(column=2,row=12)
        #Direccion del instrumento
        self.ventana.etiq13=Label(self.ventana, text="Direccion del instrumento: $"+columnas[13])
        self.ventana.etiq13.grid(column=1,row=13,sticky="E")
        self.ventana.centr13=Entry(self.ventana, width=30)
        self.ventana.centr13.grid(column=2,row=13)
        self.ventana.centr13.insert(0,"192.168.1.25")
        #Mascara de Subred
        self.ventana.etiq14=Label(self.ventana, text="Mascara de Subred: $"+columnas[14])
        self.ventana.etiq14.grid(column=1,row=14,sticky="E")
        self.ventana.centr14=Entry(self.ventana, width=30)
        self.ventana.centr14.grid(column=2,row=14)
        self.ventana.centr14.insert(0,"255.255.255.0")
        #Puerto de Comunicaiones
        self.ventana.etiq15=Label(self.ventana, text="Puerto de Comunicaciones: $"+columnas[15])
        self.ventana.etiq15.grid(column=1,row=15,sticky="E")
        self.ventana.centr15=Entry(self.ventana, width=30)
        self.ventana.centr15.grid(column=2,row=15)
        self.ventana.centr15.insert(0,"502")
        #ID de comunicacion
        self.ventana.etiq16=Label(self.ventana, text="ID de comunicacion: $"+columnas[16])
        self.ventana.etiq16.grid(column=1,row=16,sticky="E")
        self.ventana.centr16=Entry(self.ventana, width=30)
        self.ventana.centr16.grid(column=2,row=16)
        self.ventana.centr16.insert(0,"1")
        #Tabla de Linealizacion
        self.ventana.etiq17=Label(self.ventana, text="Tabla de Linealizacion (X:Y) $"+columnas[17])
        self.ventana.etiq17.grid(column=1,row=17,sticky="E")
        self.ventana.centr17=Entry(self.ventana, width=30)
        self.ventana.centr17.insert(0,"0:0,1:1,2:2,3:3")
        self.ventana.centr17.grid(column=2,row=17)
        self.ventana.mainloop()
    def client_exit(self):
        exit()
    def acerca_de(self):
        MessageBox.showinfo("Acerca de..", " Proyecto Roraima \n Jul-2021 \n Miguel Angel Aguirre")
    def database_connect(self):
        try:
            connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
            cursor=connection.cursor()
            MessageBox.showinfo("Success", "Conexion Exitosa")
        except:
            MessageBox.showinfo("Error", "Fallo de Conexion")

#creation of an instance
app = Window()
