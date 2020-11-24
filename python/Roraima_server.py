import mysql.connector
import logging
from datetime import datetime
from pymodbus.client.sync import ModbusTcpClient
import time

#PASO 1: CONOCER LA LISTA DE SENSORES
connection=mysql.connector.connect (host='192.168.1.20',database='MAIN_SENSOR',user='remoto',password='12345')
cursor=connection.cursor()
cursor.execute("SELECT DB_SENSOR FROM MAIN WHERE 1")
LISTA_SENSORES=cursor.fetchall()
connection.close()

#PASO 2: CONOCER LA LISTA DE ULTIMOS ID PARA CADA SENSOR
i=0;
connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
cursor=connection.cursor()
for SENSOR in LISTA_SENSORES[:][0]:
    cursor.execute("SELECT COUNT(*) FROM "+ SENSOR +"_MEASURE")
    conteo=cursor.fetchone()
    LAST_ID=1
    if conteo[0] > 0:
    cursor.execute("SELECT ID FROM "+ SENSOR +"_MEASURE ORDER BY ID DESC LIMIT 1")
    LAST_ID[i]=cursor.fetchone()
    i=i+1
connection.close()

#PASO 3: TRAER LOS ULTIMOS REGISTROS SEGUN LA LISTA DE ID DE CADA SENSOR
connection=mysql.connector.connect (host='192.168.1.20',database='MAIN_SENSOR',user='remoto',password='12345')
cursor=connection.cursor()
i=0
for SENSOR in LISTA_SENSORES[:][0]:
    cursor.execute("SELECT * FROM "+ SENSOR +"_CONF WHERE 1")
    CONF = cursor.fetchall()
    CANT_DIR=len(CONF)
    TAGS=[V[2] for V in CONF[6:CANT_DIR]]
    cursor.execute("SELECT * FROM "+ SENSOR +"_MEASURE WHERE ID > LAST_ID[i]")
    MEDICIONES[i]=cursor.fetchall()
    i=i+1
connection.close()

#paso 4: INSERTAR LOS ULTIMOS REGISTRS EN LA LISTA LOCAL
connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
cursor=connection.cursor()
i=0
for SENSOR in LISTA_SENSORES[:][0]:
    Q1="INSERT INTO `"+ SENSOR + "_MEASURE`  (`ID`, `FECHA_HORA`"
    Q2= ")  VALUES ('"+ str(LAST_ID[i]) + "','" + str(fecha)+"'"
    i=0;
    for j in range(len(TAGS)):
        Q1=Q1+ ",`" + TAGS[i]+"`"
        Q2=Q2+ ",'" + str(result[i][0])+"'"
        i+=1
    Query=Q1+Q2+")"
connection.close()

#cursor.execute(Query)
#connection.commit()
