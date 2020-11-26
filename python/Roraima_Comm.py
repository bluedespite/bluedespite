#!/usr/bin/env python3
import mysql.connector
import logging
from datetime import datetime
from pymodbus.client.sync import ModbusTcpClient
import time
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600)

FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')

logging.basicConfig(filename='/home/pi/Documents/git_files/python/log_modbus', filemode='w',format=FORMAT)
log=logging.getLogger()
log.setLevel(logging.DEBUG)

def Roraima_communications():
#if True:ddf
     while True:
#    if True:
        t0=time.time()
        comando = datetime.now().strftime("%d%b,%H:%M:%S+")
        comando+='\n'
        error_AN=0
        try:
            a=arduino.write(comando.encode())
            lectura = arduino.readline()
            txt=str(lectura)
            txt=txt[2:-5]
            analogico=txt.split("|")
        except:
            logging.error("No se puede contectar a Tarjeta ARDUINO")
            analogico=[]
            analogico.append(0)
            analogico.append(0)
            analogico.append(0)
            analogico.append(0)
            analogico.append(0)
            analogico.append(0)
            error_AN=1
        error_bd=0
        try:
            connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
            cursor=connection.cursor()
            cursor.execute("SELECT DB_SENSOR FROM MAIN WHERE 1")
            LISTA_SENSORES=cursor.fetchall()
        except:
            logging.error("No se puede contectar a base de datos Main Sensor de este dispositivo")
            error_bd=1
        i=0
        if error_bd==0:
            for SENSOR in LISTA_SENSORES[:][0]:
                error_general=0
                cursor.execute("SELECT * FROM "+ SENSOR +"_CONF WHERE 1")
                CONF = cursor.fetchall()
                CANT_DIR=len(CONF)
                TAGS=[T[1] for T in CONF]
                RANG_MIN=[T[4] for T in CONF]
                RANG_MAX=[T[5] for T in CONF]
                PROTOCOLO=[T[6] for T in CONF]
                DIRECCION=[T[7] for T in CONF]
                PARAM_COMM1=[T[8] for T in CONF]
                PARAM_COMM2=[T[9] for T in CONF]
                PARAM_COMM3=[T[10] for T in CONF]
                PARAM_COMM4=[T[11] for T in CONF]
                PARAM_COMM5=[T[12] for T in CONF]
                PARAM_COMM6=[T[13] for T in CONF]
                result=[];
                for j in range(len(TAGS)):
                    if PROTOCOLO[j]=="MTCP":
                        client = ModbusTcpClient(DIRECCION[j],port=int(PARAM_COMM3[j]))
                        cnx_modbus=client.connect()
                        if cnx_modbus== True:
                            X_1=int(PARAM_COMM5[j])-40001
                            rr=0
                            try:
                                rr = client.read_holding_registers(X_1,1,unit=int(PARAM_COMM4[j]))
                                result.append(rr.registers[0])
                            except:
                                logging.exception("No se puede leer registros: " + SENSOR + ":" + TAGS[j])
                                error_general=1
                                result.append(0)
                        else:
                            logging.exception("No se puede conectar: " + SENSOR + ":" + TAGS[j])
                            error_general=1
                            result.append(0)
                    if PROTOCOLO[j]=="ANA":
                        canaltxt=DIRECCION[j]
                        canal=int(canaltxt)
                        if float(analogico[canal])>(1024/5):
                            rANA=(float(analogico[canal])-(1024/5))/(1024-(1024/5))
                            rMed=rANA*(float(RANG_MAX[j])-float(RANG_MIN[j]))+float(RANG_MIN[j])
                            result.append(rMed)
                        else:
                            result.append(0)
                            logging.error("Error en sensor Analogico : " + SENSOR +":"+TAGS[j]+":"+DIRECCION[j])
                fecha=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute("SELECT COUNT(*) FROM "+ SENSOR +"_MEASURE")
                conteo=cursor.fetchone()
                LAST_ID=1
                if conteo[0] !=0:
                    cursor.execute("SELECT ID FROM "+ SENSOR +"_MEASURE ORDER BY ID DESC LIMIT 1")
                    LID=cursor.fetchone()
                    LAST_ID=LID[0]+1
                Q1="INSERT INTO `"+ SENSOR + "_MEASURE`  (`ID`, `FECHA_HORA`"
                Q2= ")  VALUES ('"+ str(LAST_ID) + "','" + str(fecha)+"'"
                for j in range(len(TAGS)):
                    Q1=Q1+ ",`" + TAGS[j]+"`"
                    Q2=Q2+ ",'" + str(result[j])+"'"
                Query=Q1+Q2+")"
                cursor.execute(Query)
                connection.commit()
                logging.info("Se actualizo: "+ SENSOR + ","+ str(len(TAGS)) + " TAGS")
                connection.close()
        t1=time.time()
        while((t1-t0)<60):
            t1=time.time()
            comando = datetime.now().strftime("%d%b,%H:%M:%S+")
            comando+='\n'
            try:
                a=arduino.write(comando.encode())
            except:
                logging.error("No se puede contectar a Tarjeta ARDUINO")

try:
    Roraima_communications()
except (KeyboardInterrupt):
    logging.debug("Interrupcion por Teclado. Finalizando")
    exit()
