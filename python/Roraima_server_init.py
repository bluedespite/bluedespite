#!/usr/bin/env python3
import mysql.connector
connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
cursor=connection.cursor()
print("***Configuracion Inicial***")
while True:
    n=input("Seleccione si es la Primera vez que corre la inicializacion(S/n):")
    if n=="S":
        sql_select_Query= "CREATE OR REPLACE TABLE `MAIN_SERVER` ( `ID` INT NOT NULL , `DIRECCION_IP` TEXT NOT NULL , INDEX `ID` (`ID`)) ENGINE = InnoDB"
        cursor.execute(sql_select_Query)
        sql_select_Query= "CREATE OR REPLACE TABLE `MAIN_DB` ( `ID` INT NOT NULL , `TABLA` TEXT NOT NULL , INDEX `ID` (`ID`)) ENGINE = InnoDB"
        cursor.execute(sql_select_Query)
        sql_select_Query= "CREATE OR REPLACE TABLE `USUARIOS` ( `ID` INT NOT NULL , `NOMBRE` TEXT NOT NULL ,`Email` TEXT NOT NULL ,`Password` TEXT NOT NULL , INDEX `ID` (`ID`)) ENGINE = InnoDB"
        cursor.execute(sql_select_Query)
        print("+++Configuracion de Usuarios +++")
        while True:
            n=input("Introduzca Cantidad de usuarios a Crear:")
            try:
                numero=int(n)
                if numero>=1:
                    break
            except:
                numero=0
        for j in range(numero):
            while True:
                Nombre=input("Introduzca el Nombre del Usuario No "+ str(j+1) + " :")
                Email=input("Introduzca el Email del Usuario No "+ str(j+1) + " :")
                Contraseña=input("Introduzca la contaseña del Usuario No "+ str(j+1) + " :")
                if (Nombre!="" and Email!="" and Contraseña!=""):
                    sql = "INSERT INTO `USUARIOS`  (ID, `Nombre`, `Email`, `Password`) VALUES (%s, %s, %s, %s)"
                    val = (str(j+1), Nombre,Email,Contraseña)
                    cursor.execute(sql,val)
                    break
        connection.commit()
        break
    if n=="n":
        break


print("+++Configuracion del Servidor +++")
while True:
    n=input("Introduzca la cantidad de Controladores Remotos:")
    try:
        numero=int(n)
        if numero>=1:
            break
    except:
        numero=0
for j in range(numero):
    while True:
        DIRECCION=input("Introduzca la direccion IP del sensor# "+ str(j+1) + " .eje. xx.xx.xx.xx:")
        try:
            nn=DIRECCION.split(".")
            numero=int(nn[0])+int(nn[1])+int(nn[2])+int(nn[3])
            if numero>1:
                sql = "INSERT INTO `MAIN_SERVER`  (ID, `DIRECCION_IP`) VALUES (%s, %s)"
                val = (str(j+1), DIRECCION)
                cursor.execute(sql,val)
                break
        except:
            numero=0
connection.commit()
