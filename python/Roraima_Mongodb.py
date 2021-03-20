#!/usr/bin/env python3
import logging
from datetime import datetime
from pymodbus.client.sync import ModbusTcpClient
import time
import serial
import serial.tools.list_ports
from pymongo import MongoClient

if True:
    FORMAT = ('%(asctime)-15s %(threadName)-15s ' '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
    logging.basicConfig(filename='/home/pi/Documents/git_files/python/log_modbus', filemode='w',format=FORMAT)
    log=logging.getLogger()
    log.setLevel(logging.DEBUG)
    for p in serial.tools.list_ports.comports():
        try:
            if 'Arduino' in p.manufacturer:
                arduino_ports = p.device
                logging.info("Puerto Serie Arduino:"+str(p.device))
                break
        except:
            break
    time.sleep(2)
    logging.info("Info Puerto Serie Arduino:"+str(p.device))
    arduino = serial.Serial(arduino_ports,9600, timeout=5)
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
        client=MongoClient(mongodb+srv://MongoAdmin:12345@cluster0.m3fmw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority)
    except:
        logging.error("No se puede contectar a Base de Datos Remota")
        error_bd=1
    
