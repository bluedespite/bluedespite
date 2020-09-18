import mysql.connector
import logging
from datetime import datetime
from pymodbus.client.sync import ModbusTcpClient
import time

FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(filename='log_modbus', filemode='w',format=FORMAT)
log=logging.getLogger()
log.setLevel(logging.DEBUG)

def Roraima_communications():
#if True:
    while True:
#    if True:
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
                TAGS=[T[1] for T in CONF[0:14]]
                VALORES=[V[2] for V in CONF[0:14]]
                zipobj=zip(TAGS,VALORES)
                D_CONF=dict(zipobj)
                DIRE=[T[1] for T in CONF[14:CANT_DIR]]
                TAGS=[V[2] for V in CONF[14:CANT_DIR]]
                result=[0]*len(DIRE)
                if D_CONF['PROTOCOLO']=='MODBUS_TCP':
                    client = ModbusTcpClient(D_CONF['ADDRESS_IP'],port=int(D_CONF['PORT_TCP']))
                    cnx_modbus=client.connect()
                    result=list();
                    if cnx_modbus== True:
                        for x in DIRE:
                            rr=0
                            X_1=int(x)-40001
                            try:
                                rr = client.read_holding_registers(X_1,1,unit=int(D_CONF['ID']))
                                result.append(rr.registers)
                            except:
                                logger.exception("No se puede leer registros: " + SENSOR + ":" + x)
                                error_general=1
                                break
                    else:
                        error_general=1
                        logging.error("No se puede conectar: " + SENSOR )
                else:
                    logging.debug("Protocolo no implementado aun: " + D_CONF['PROTOCOLO'])
                    error_general=1
                if error_general==0:
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
                        i=0;
                        for j in range(len(TAGS)):
                            Q1=Q1+ ",`" + TAGS[i]+"`"
                            Q2=Q2+ ",'" + str(result[i][0])+"'"
                            i+=1
                        Query=Q1+Q2+")"
                        cursor.execute(Query)
                        connection.commit()
                        logging.info("Se actualizo: "+ SENSOR + ","+ str(len(TAGS)) + " TAGS")
                connection.close()
        time.sleep(10)

try:
    Roraima_communications()
except (KeyboardInterrupt):
    logging.debug("Interrupcion por Teclado. Finalizando")
    exit()
