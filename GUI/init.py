from tkinter import *
import mysql.connector
from tkinter import messagebox as MessageBox
from tkinter import ttk, font
import pandas as pd
import numpy as np

df = pd.DataFrame({'ID': [],'ESTACION': [], 'ID_ESTACION': [], 'TANQUE':[], 'ID_TANQUE':[], 'PRODUCTO':[], 'DENSIDAD':[], 'TAG_SENSOR':[],'DESCRIPCION':[],'UM':[], 'RANGO_MIN':[], 'RANGO_MAX':[],'TIPO':[],'DIRECCION':[],'MASCARA':[],'PUERTO':[],'ID_COMM':[],'LINEALIZACION':[]})
columnas=list(df.keys())
class Window:
    def __init__(self):
        self.ventana=Tk()
        self.ventana.geometry("800x400")
        self.ventana.title("Configuracion Inicial")
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
        #Estacion
        self.ventana.etiq=[]
        self.ventana.centr=[]
        for i in range(len(columnas)):
            self.ventana.etiq.append(Label(self.ventana, text=columnas[i]))
            self.ventana.etiq[i].grid(column=1,row=2*i)
            self.ventana.centr.append(Entry(self.ventana, width=30))
            self.ventana.centr[i].grid(column=2,row=2*i)
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
