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
    if True:
        try:
            connection_local=mysql.connector.connect (host='localhost',database='MAIN_SERVER', user='admin',password='12345')
            cursor_local=connection_local.cursor()
            cursor_local.execute("SELECT DIRECCION_IP FROM MAIN_SERVER WHERE 1")
            LISTA_DIRECCIONES=cursor_local.fetchall()
            cursor_local.execute("SHOW TABLES")
            DBS=cursor_local.fetchall()
        except:
            logging.error("No se puede contectar a base de datos main_server del servidor central")
            #break
        for direccion in LISTA_DIRECCIONES[:][0]:
            error_general=0;
            try:
                connection_remoto=mysql.connector.connect (host=direccion ,database='MAIN_SENSOR',user='remoto',password='12345')
                cursor_remoto=connection_remoto.cursor()
                cursor_remoto.execute("SELECT DB_SENSOR FROM MAIN WHERE 1")
                LISTA_SENSORES=cursor_remoto.fetchall()
            except:
                logging.error("No se puede contectar a base de datos main_server del servidor: "+str(direccion))
                error_general=1
            j=0
            if error_general==0:
                for SENSOR in LISTA_SENSORES[:][0]:
                    j=j+1
                    Query="SELECT * FROM "+ SENSOR +"_CONF WHERE 1"
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
                    prueba=SENSOR+"_MEASURE"
                    for DB in DBS[:][0]:
                        if DB[0] == prueba:
                            flag=True
                    if flag == False:
                        sql_select_Query="CREATE OR REPLACE TABLE `MAIN_SENSOR`.`"+ SENSOR + "_MEASURE` ( `ID` INT NOT NULL ,`FECHA_HORA` DATETIME NOT NULL"
                        for n in TAGS:
                            sql_select_Query= sql_select_Query + ", `" + n + "` FLOAT NOT NULL"
                        sql_select_Query=sql_select_Query + "  , INDEX `ID` (`ID`)) ENGINE = InnoDB"
                        cursor_local.execute(sql_select_Query)
                    cursor_local.execute("SELECT COUNT(*) FROM MAIN_SENSOR."+ SENSOR +"_MEASURE")
                    conteo=cursor_local.fetchone()
                    LAST_ID=0
                    if conteo[0] > 0:
                        cursor_local.execute("SELECT ID FROM MAIN_SENSOR."+ SENSOR +"_MEASURE ORDER BY ID DESC LIMIT 1")
                    Query="SELECT * FROM "+ SENSOR +"_MEASURE WHERE `ID` > "+str(LAST_ID)
                    cursor_remoto.execute(Query)
                    LAST_ID=cursor_local.fetchone()
                    val=cursor_remoto.fetchall()
                    Q1="INSERT INTO MAIN_SENSOR."+ SENSOR + "_MEASURE  (`ID`, `FECHA_HORA`"
                    Q2= ")  VALUES (%s,%s"
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
        time.sleep(600)
try:
    Roraima_Server()
except:
    logging.error("Finalizado")
    exit()
