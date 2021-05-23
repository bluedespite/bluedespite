#!/usr/bin/env python3
import mysql.connector
import logging
from datetime import datetime
from pymodbus.client.sync import ModbusTcpClient
import time
import serial
import serial.tools.list_ports

LAST_VALID_LON=0
LAST_VALID_LAT=0

def Roraima_communications():
    FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
    logging.basicConfig(filename='Roraima_Log.txt', filemode='w',format=FORMAT)
    log=logging.getLogger()
    log.setLevel(logging.DEBUG)
    for p in serial.tools.list_ports.comports():
        try:
            if 'Arduino' in p.manufacturer:
                arduino_ports = p.device
                logging.info("Puerto Serie Arduino:"+str(p.device))
                break
        except:
            logging.error("No se puede contectar a Tarjeta ARDUINO")
            break
    time.sleep(2)
    logging.info("Info Puerto Serie Arduino:"+str(p.device))
    while True:
        arduino = serial.Serial(arduino_ports,9600, timeout=50)
        t0=time.time()
        error_AN=0
        arduinos={}
        try:
            while(True):
                lectura = arduino.readline()
                txt=str(lectura)
                txt=txt[2:-5]
                if txt.find('Latitude')<0:
                    logging.info("Error de lectura en cadena Serial")
                else:
                    break
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
        except:
            logging.error("No se puede contectar a Tarjeta ARDUINO")
            break
            error_AN=1
        error_bd=0
        fecha=arduinos["DateTime"]
        analogico=[]
        analogico.append(int(arduinos["Analog0"]))
        analogico.append(int(arduinos["Analog1"]))
        analogico.append(int(arduinos["Analog2"]))
        analogico.append(int(arduinos["Analog3"]))
        analogico.append(int(arduinos["Analog4"]))
        analogico.append(int(arduinos["Analog5"]))
        try:
            connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
            cursor=connection.cursor()
            cursor.execute("SELECT ID_TANQUE FROM ESTACION WHERE 1")
            LISTA_SENSORES=cursor.fetchall()
        except:
            logging.error("No se puede contectar a base de datos Main Sensor de este dispositivo")
            error_bd=1
        i=0
        if error_bd==0:
            for SENSOR in LISTA_SENSORES:
                error_general=0
                cursor.execute("SELECT * FROM "+ SENSOR[:][0] +"_CONF WHERE 1")
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
                                logging.exception("No se puede leer registros: " + SENSOR[:][0] + ":" + TAGS[j])
                                error_general=1
                                result.append(0)
                        else:
                            logging.exception("No se puede conectar: " + SENSOR[:][0] + ":" + TAGS[j])
                            error_general=1
                            result.append(0)
                    if PROTOCOLO[j]=="ANA":
                        canaltxt=DIRECCION[j]
                        canal=int(canaltxt)
                        try:
                            if float(analogico[canal])>(1024/5):
                                rANA=(float(analogico[canal])-(1024/5))/(1024-(1024/5))
                                rMed=rANA*(float(RANG_MAX[j])-float(RANG_MIN[j]))+float(RANG_MIN[j])
                                result.append(rMed)
                            else:
                                result.append(0)
                                logging.error("Error en sensor Analogico : " + SENSOR[:][0] +":"+TAGS[j]+":"+DIRECCION[j])
                        except:
                            result.append(0)
                            logging.error("Error en sensor Analogico : " + SENSOR[:][0] +":"+TAGS[j]+":"+DIRECCION[j])
                cursor.execute("SELECT COUNT(*) FROM "+ SENSOR[:][0] +"_MEASURE")
                conteo=cursor.fetchone()
                LAST_ID=1
                if conteo[0] !=0:
                    cursor.execute("SELECT ID FROM "+ SENSOR[:][0] +"_MEASURE ORDER BY ID DESC LIMIT 1")
                    LID=cursor.fetchone()
                    LAST_ID=LID[0]+1
                Q1="INSERT INTO `"+ SENSOR[:][0] + "_MEASURE`  (`ID`, `FECHA_HORA`, `LAT`, `LON`, `VEL`"
                Q2= ")  VALUES ('"+ str(LAST_ID) + "','" + str(fecha)+ "','" + str(arduinos["Latitude"])+ "','" + str(arduinos["Longitude"])+ "','" + str(arduinos["Velocity"])+"'"
                for j in range(len(TAGS)):
                    Q1=Q1+ ",`" + TAGS[j]+"`"
                    Q2=Q2+ ",'" + str(result[j])+"'"
                Query=Q1+Q2+")"
                cursor.execute(Query)
                connection.commit()
                logging.info("Se actualizo: "+ SENSOR[:][0] + ","+ str(len(TAGS)) + " TAGS")
        connection.close()
        arduino.flush()
        t1=time.time()
        break
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
    exit()
