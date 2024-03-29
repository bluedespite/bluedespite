#!/usr/bin python3

import mysql.connector
import logging
from datetime import datetime
from pymodbus.client.sync import ModbusTcpClient
import time

FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')

logging.basicConfig(filename='log_server.txt', filemode='w',format=FORMAT)
log=logging.getLogger()
log.setLevel(logging.DEBUG)

def Roraima_Server():
    while True:
        time.sleep(300)
        try:
            connection_local=mysql.connector.connect (host='localhost',database='MAIN_SERVER', user='admin',password='12345')
            cursor_local=connection_local.cursor()
            cursor_local.execute("SELECT DIRECCION_IP FROM MAIN_SERVER WHERE 1")
            LISTA_DIRECCIONES=cursor_local.fetchall()
            cursor_local.execute("SHOW TABLES")
            DBS=cursor_local.fetchall()
        except:
            logging.error("No se puede contectar a base de datos main_server del servidor central")
        for direccion in LISTA_DIRECCIONES:
            error_general=0
            try:
                connection_remoto=mysql.connector.connect (host=direccion[:][0] ,database='MAIN_SENSOR',user='remoto',password='12345')
                cursor_remoto=connection_remoto.cursor()
                cursor_remoto.execute("SELECT ID_TANQUE FROM ESTACION WHERE 1")
                LISTA_SENSORES=cursor_remoto.fetchall()
            except:
                logging.error("No se puede contectar a base de datos ESTACION del servidor: "+str(direccion[:][0]))
                error_general=1
            j=0
            if error_general==0:
                for SENSOR in LISTA_SENSORES:
                    j=j+1
                    Query="SELECT * FROM "+ SENSOR[:][0] +"_CONF WHERE 1"
                    cursor_local.execute(Query)
                    CONF = cursor_local.fetchall()
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
                    flag=False
                    prueba=SENSOR[:][0]+"_MEASURE"
                    for DB in DBS:
                        if DB[0][:] == prueba:
                            flag=True
                    if flag == False:
                        sql_select_Query="CREATE OR REPLACE TABLE `MAIN_SERVER`.`"+ SENSOR[:][0] + "_MEASURE` ( `ID` INT NOT NULL ,`FECHA_HORA` DATETIME NOT NULL,`LAT` FLOAT NULL, `LON` FLOAT NOT NULL,`VEL` FLOAT NOT NULL"
                        for n in TAGS:
                            sql_select_Query= sql_select_Query + ", `" + n + "` FLOAT NOT NULL"
                        sql_select_Query=sql_select_Query + "  , INDEX `ID` (`ID`)) ENGINE = InnoDB"
                        cursor_local.execute(sql_select_Query)
                    cursor_local.execute("SELECT COUNT(*) FROM MAIN_SERVER."+ SENSOR[:][0] +"_MEASURE")
                    conteo=cursor_local.fetchone()
                    LAST_ID=0
                    if conteo[0] > 0:
                        cursor_local.execute("SELECT ID FROM MAIN_SERVER."+ SENSOR[:][0] +"_MEASURE ORDER BY ID DESC LIMIT 1")
                        LID=cursor_local.fetchone()
                        LAST_ID=LID[0]
                    Query="SELECT * FROM "+ SENSOR[:][0] +"_MEASURE WHERE `ID` > "+str(LAST_ID)
                    cursor_remoto.execute(Query)
                    val=cursor_remoto.fetchall()
                    Q1="INSERT INTO MAIN_SERVER."+ SENSOR[:][0] + "_MEASURE  (`ID`, `FECHA_HORA`, `LAT`, `LON`, `VEL`"
                    Q2= ")  VALUES (%s,%s,%s,%s,%s"
                    for t in TAGS:
                        Q1=Q1+ ",`" + t +"`"
                        Q2=Q2+ ",%s"
                    Query=Q1+Q2+")"
                    len_val=[T[0] for T in val]
                    for j in range(len(len_val)):
                        cursor_local.execute(Query,val[j])
                    connection_local.commit()
                connection_remoto.close()
                connection_local.close()
        logging.info("Se actualizo registros")
try:
    Roraima_Server()
except:
    logging.error("Finalizado por Error")
    exit()
