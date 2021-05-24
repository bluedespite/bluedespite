#!/usr/bin python3
import mysql.connector
print("***Configuracion Inicial Servidor***")

try:
    connection=mysql.connector.connect (host='localhost',database='MAIN_SERVER',user='admin',password='12345')
    cursor=connection.cursor()
except:
    print("No se puede contectar a base de datos MAIN_SERVER del servidor central")

while True:
    n=input("Seleccione si es la Primera vez que corre la inicializacion(S/n):")
    if n=="S":
        sql_select_Query= "CREATE OR REPLACE TABLE `MAIN_SERVER` ( `ID` INT NOT NULL , `DIRECCION_IP` TEXT NOT NULL , INDEX `ID` (`ID`)) ENGINE = InnoDB"
        cursor.execute(sql_select_Query)
        sql_select_Query= "CREATE OR REPLACE TABLE `USUARIOS` ( `ID` INT NOT NULL , `NOMBRE` TEXT NOT NULL ,`Email` VARCHAR(32) NOT NULL ,`Password` VARCHAR(32) NOT NULL , INDEX `ID` (`ID`)) ENGINE = InnoDB"
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
                Contrasena=input("Introduzca la contaseña del Usuario No "+ str(j+1) + " :")
                if (Nombre!="" and Email!="" and Contrasena!=""):
                    sql = "INSERT INTO `USUARIOS`  (ID, `Nombre`, `Email`, `Password`) VALUES (%s, %s, MD5(%s), MD5(%s))"
                    val = (str(j+1), Nombre,Email,Contrasena)
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
cursor.execute("SELECT DIRECCION_IP FROM MAIN_SERVER WHERE 1")
LISTA_DIRECCIONES=cursor.fetchall()
for direccion in LISTA_DIRECCIONES:
	error_general=0;
	try:
		connection_remoto=mysql.connector.connect (host=direccion[:][0] ,database='MAIN_SENSOR',user='remoto',password='12345')
		cursor_remoto=connection_remoto.cursor()
		cursor_remoto.execute("SELECT ID_TANQUE FROM ESTACION WHERE 1")
		LISTA_SENSORES=cursor_remoto.fetchall()
	except:
		print("ERROR: No se puede contectar a base de datos ESTACION del servidor: "+str(direccion[:][0]))
		error_general=1
	if error_general==0:
		k=0
		for SENSOR in LISTA_SENSORES:
			k=k+1
			Query="SELECT * FROM "+ SENSOR[:][0] +"_CONF WHERE 1"
			cursor_remoto.execute(Query)
			CONF = cursor_remoto.fetchall()
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
			sql_select_Query= "CREATE OR REPLACE TABLE `"+ SENSOR[:][0] + "_CONF` ( `ID` INT NOT NULL , `TAG` TEXT NOT NULL ,`DESCRIPCION` TEXT NOT NULL , `UNITS` TEXT NOT NULL , `RANG_MIN` TEXT NOT NULL , `RANG_MAX` TEXT NOT NULL, `PROTOCOLO` TEXT NOT NULL,`DIRECCION` TEXT NOT NULL, `PARAM_COMM1` TEXT NOT NULL, `PARAM_COMM2` TEXT NOT NULL,`PARAM_COMM3` TEXT NOT NULL,`PARAM_COMM4` TEXT NOT NULL,`PARAM_COMM5` TEXT NOT NULL,`PARAM_COMM6` TEXT NOT NULL,   INDEX `ID` (`ID`)) ENGINE = InnoDB"
			cursor.execute(sql_select_Query)
			for j in range(len(TAGS)):
				Query= "INSERT INTO `"+ SENSOR[:][0] + "_CONF` (`ID`, `TAG`, `DESCRIPCION`,`UNITS`,`RANG_MIN`,`RANG_MAX`,`PROTOCOLO`,`DIRECCION`,`PARAM_COMM1`,`PARAM_COMM2`,`PARAM_COMM3`,`PARAM_COMM4`,`PARAM_COMM5`,`PARAM_COMM6`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
				cursor.execute(Query,CONF[j])
			connection.commit()
