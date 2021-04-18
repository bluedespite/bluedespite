#Se debe e crear la primera vez la Base de datos MAIN_SENSOR mediante el phpmyadmin
#se debe instalar el mysql CONECTOR pip3 install mysql-connector-python
#descomentar los codigos de primera vez que se usa:

import mysql.connector
connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
cursor=connection.cursor()
print("***Configuracion Inicial***")
print("***El Programa de incializacion tiene tres componentes posibles: Bahia fija, Cisterna o Vehiculo***")

while True:
    n=input("Seleccione si es la Primera vez que corre la inicializacion(S/n):")
    if n=="S":
        sql_select_Query= "CREATE OR REPLACE TABLE `ESTACION` ( `ID` INT NOT NULL , `ESTACION` TEXT NOT NULL ,`ID_ESTACION` TEXT NOT NULL,`ID_TANQUE` TEXT NOT NULL, `ID_PRODUCTO` TEXT NOT NULL,`CAPACIDAD` INT NOT NULL,`DENSIDAD` FLOAT NOT NULL, INDEX `ID` (`ID`)) ENGINE = InnoDB"
        cursor.execute(sql_select_Query)
        sql_select_Query= "CREATE OR REPLACE TABLE `MAIN` ( `ID` INT NOT NULL , `DB_SENSOR` TEXT NOT NULL,   INDEX `ID` (`ID`)) ENGINE = InnoDB"
        cursor.execute(sql_select_Query)
        break
    if n=="n":
        break
TAG_SENSOR=[]
print("+++Configuracion de componentes +++")
while True:
    n=input("Desea configurar una Bahia Fija (B), una Cisterna (C) o Vehiculo (V): ")
    if n=="B":
        ESTACION="BAHIA"
        ENABLE_RENDIMIENTO="F"
        break
    if n=="C":
        ESTACION="CISTERNA"
        ENABLE_RENDIMIENTO="T"
        break
    if n=="V":
        ESTACION="VEHICULO"
        ENABLE_RENDIMIENTO="T"
        break

while True:
    ID_ESTACION=input("Introduce el ID de "+ESTACION+" : ")
    if ID_ESTACION !="":
        break
if ESTACION=="VEHICULO":
    n_tanques=1
    ID_TANQUE=ID_ESTACION
    while True:
        CAPACIDAD=input("Indique la capacidad del tanque: ")
        try:
            if int(CAPACIDAD) > 0:
                break
        except:
            CAPACIDAD=0
    while True:
        ID_PRODUCTO=input("Indique el ID del producto del tanque: ")
        if ID_PRODUCTO!="":
            break
    while True:
        DENSIDAD=input("Indique la densidad del producto del tanque: ")
        try:
            if int(DENSIDAD) > 0:
                break
        except:
            DENSIDAD=0
    sql_select_Query="INSERT INTO ESTACION (`ID`, `ESTACION`,`ID_ESTACION`, `ID_TANQUE`,`ID_PRODUCTO`,`CAPACIDAD`,`DENSIDAD`) VALUES (1,'"+ ESTACION +"','"+ ID_ESTACION +"','"+ ID_TANQUE +"','"+ ID_PRODUCTO +"','"+ CAPACIDAD +"','"+ DENSIDAD +"')"
    TAG_SENSOR.append(ID_ESTACION)
else:
    while True:
        n=input("Indique el numero de Tanques de "+ ESTACION + " " + ID_ESTACION +": ")
        try:
            n_tanques=int(n)
            if n_tanques>0:
                break
        except:
            n_tanques=0
    for j in range(n_tanques):
        while True:
            ID_TANQUE=input("Indique el ID del tanque " + str(j) + " : ")
            if ID_TANQUE!="":
                TAG_SENSOR.append(ID_TANQUE)
                break
        while True:
            CAPACIDAD=input("Indique la capacidad del tanque" + str(j) +": ")
            try:
                if int(CAPACIDAD) > 0:
                    break
            except:
                CAPACIDAD=0
        while True:
            ID_PRODUCTO=input("Indique el ID del producto del tanque" + str(j) +": ")
            if ID_PRODUCTO!="":
                break
        while True:
            DENSIDAD=input("Indique la densidad del producto del tanque" + str(j) +": ")
            try:
                if int(DENSIDAD) > 0:
                    break
            except:
                DENSIDAD=0
        sql_select_Query="INSERT INTO ESTACION (`ID`, `ESTACION`,`ID_ESTACION`, `ID_TANQUE`,`ID_PRODUCTO`,`CAPACIDAD`,`DENSIDAD`) VALUES ("+ str(j+1) +",'"+ ESTACION +"','"+ ID_ESTACION +"','"+ ID_TANQUE +"','"+ ID_PRODUCTO +"','"+ CAPACIDAD +"','"+ DENSIDAD +"')"
        cursor.execute(sql_select_Query)
        connection.commit()
print("******Configuracion de los instrumentos por tanque*****")
print("******(El sensor de NIVEL DEBE SER EL PRIMER INSTRUMENTO OJO)*****")
for T_SENSOR in TAG_SENSOR:
    sql_select_Query= "CREATE OR REPLACE TABLE `MAIN_SENSOR`.`"+ T_SENSOR + "_CONF` ( `ID` INT NOT NULL , `TAG` TEXT NOT NULL ,`DESCRIPCION` TEXT NOT NULL , `UNITS` TEXT NOT NULL , `RANG_MIN` TEXT NOT NULL , `RANG_MAX` TEXT NOT NULL, `PROTOCOLO` TEXT NOT NULL,`DIRECCION` TEXT NOT NULL, `PARAM_COMM1` TEXT NOT NULL, `PARAM_COMM2` TEXT NOT NULL,`PARAM_COMM3` TEXT NOT NULL,`PARAM_COMM4` TEXT NOT NULL,`PARAM_COMM5` TEXT NOT NULL,`PARAM_COMM6` TEXT NOT NULL,   INDEX `ID` (`ID`)) ENGINE = InnoDB"
    cursor.execute(sql_select_Query)
    numero=0
    while True:
        n=input("Introduzca la cantidad de TAGS para el tanque " + T_SENSOR+":")
        try:
            numero=int(n)
            if numero>=1:
                break
        except:
            numero=0
    Tags=[]
    for j in range(numero):
        while True:
            TAG=input("introduce el tag " + str(j)+" :")
            if TAG!="":
                Tags.append(TAG)
                break
        while True:
            DESCRIPCION=input(" Introduce la descripcion del tag " +TAG+":")
            if DESCRIPCION!="":
                break
        while True:
            UNITS=input(" Introduce la unidad de medida del tag " +TAG+":")
            if UNITS!="":
                break
        while True:
            RANG_MIN=input (" Introduce el Rango minimo:")
            RANG_MAX=input (" Introduce el Rango maximo:")
            try:
                n1=float(RANG_MIN)
                n2=float(RANG_MAX)
                if n2>n1:
                    break
            except:
                n1=0;
                n2=0;
        while True:
            TIPO=input(" Introduce el Tipo de Comunicacion (ANA=Analogica),(MTCP=Modbus TCP), (MSER=Modus Serial):")
            if TIPO=="ANA" :
                while True:
                    DIRECCION=input("Introduzca el Canal Analogico (1-5) (canal test:0):")
                    try:
                        n1=int(DIRECCION)
                        if n1>=0 and n1<6:
                            break
                    except:
                        n1=0
                PARAM_COMM1="0"
                PARAM_COMM2="0"
                PARAM_COMM3="0"
                PARAM_COMM4="0"
                PARAM_COMM5="0"
                PARAM_COMM6="0"
                break
            if TIPO=="MTCP":
                while True:
                    DIRECCION=input("Introduzca la direccion IP del sensor .eje. xx.xx.xx.xx:")
                    try:
                        nn=DIRECCION.split(".")
                        numero=int(nn[0])+int(nn[1])+int(nn[2])+int(nn[3])
                        if numero>1:
                            break
                    except:
                        numero=0
                while True:
                    PARAM_COMM1=input("Introduzca la mascara IP  ej 255.255.255.0:")
                    try:
                        nn=PARAM_COMM1.split(".")
                        numero=int(nn[0])+int(nn[1])+int(nn[2])+int(nn[3])
                        if numero>1:
                            break
                    except:
                        numero=-1
                while True:
                    PARAM_COMM2=input("Introduzca el Gateway: ej. xxx.xxx.xxx.xxx :")
                    try:
                        nn=PARAM_COMM2.split(".")
                        numero=int(nn[0])+int(nn[1])+int(nn[2])+int(nn[3])
                        if numero>1:
                            break
                    except:
                        numero=0
                while True:
                    PARAM_COMM3=input("Introduzca el puerto de Comunicaciones: ej. 502: ")
                    try:
                        numero=int(PARAM_COMM3)
                        if numero>=1:
                            break
                    except:
                        numero=0
                while True:
                    PARAM_COMM4=input("Introduzca la ID MODBUS: ej. 1: ")
                    try:
                        numero=int(PARAM_COMM4)
                        if numero>=0:
                            break
                    except:
                        numero=-1
                while True:
                    PARAM_COMM5=input("Introduzca direccion MODBUS de la medida: ej. 40020: ")
                    try:
                        numero=int(PARAM_COMM5)
                        if numero>40000:
                            break
                    except:
                        numero=0
                PARAM_COMM6="0"
                break
        sql_select_Query= "INSERT INTO `"+ T_SENSOR + "_CONF` (`ID`, `TAG`, `DESCRIPCION`,`UNITS`,`RANG_MIN`,`RANG_MAX`,`PROTOCOLO`,`DIRECCION`,`PARAM_COMM1`,`PARAM_COMM2`,`PARAM_COMM3`,`PARAM_COMM4`,`PARAM_COMM5`,`PARAM_COMM6`) VALUES ("+ str(j+1) +",'"+ TAG +"','"+ DESCRIPCION +"','"+ UNITS +"','"+ RANG_MIN +"','"+ RANG_MAX +"','"+ TIPO +"','"+ DIRECCION +"','"+PARAM_COMM1 +"','"+ PARAM_COMM2 +"','"+ PARAM_COMM3 +"','"+ PARAM_COMM4 +"','"+ PARAM_COMM5 +"','"+ PARAM_COMM6 +"')"
        cursor.execute(sql_select_Query)
        while True:
            TABLA=input("Introduzca cantidad de puntos en tabla de linealizacion: ")
            try:
                numero=int(TABLA)
                if numero<2:
                    TABLA="2"
                    numero=2
                break
            except:
                numero=0
        print("***Tabla de linealizacion de"+TABLA+" puntos en pares (Xn,Yn)***")
        x=[]
        y=[]
        sql_select_Query="CREATE OR REPLACE TABLE `MAIN_SENSOR`.`"+ TAG + "_TABLA` ( `ID` INT NOT NULL , `ENTRADA` TEXT NOT NULL ,`SALIDA` TEXT NOT NULL ,   INDEX `ID` (`ID`)) ENGINE = InnoDB"
        cursor.execute(sql_select_Query)
        for n in range(numero):
            while True:
                x.append(input("Introduzca la medida X"+str(n)+" : "))
                y.append(input("Introduzca la medida Y"+str(n)+" : "))
                try:
                    numero=int(x[n])+int(y[n])
                    if numero>=0:
                        sql_select_Query= "INSERT INTO `"+ TAG + "_TABLA` (`ID`, `ENTRADA`, `SALIDA`) VALUES ("+ str(n+1) +",'"+ x[n] +"','"+ y[n] +"')"
                        cursor.execute(sql_select_Query)
                        break
                except:
                    numero=-1
    sql_select_Query="CREATE OR REPLACE TABLE `MAIN_SENSOR`.`"+ T_SENSOR + "_MEASURE` ( `ID` INT NOT NULL ,`FECHA_HORA` DATETIME NOT NULL"
    for n in Tags:
        sql_select_Query= sql_select_Query + ", `" + n + "` FLOAT NOT NULL"
    sql_select_Query=sql_select_Query + "  , INDEX `ID` (`ID`)) ENGINE = InnoDB"
    cursor.execute(sql_select_Query)
    sql_select_Query = ("SELECT * FROM MAIN " "WHERE DB_SENSOR = '"+T_SENSOR+"'")
    cursor.execute(sql_select_Query)
    cursor.fetchall()
    i=cursor.rowcount
    if i==0:
        cursor.execute("SELECT * FROM MAIN ORDER BY ID DESC LIMIT 1")
        aux=cursor.fetchone()
        j=cursor.rowcount
    if j<1:
        index=str(1)
    else:
        index=str(1+aux[0])
    cursor.execute("INSERT INTO `MAIN` (`ID`,`DB_SENSOR`) VALUES ("+index+",'"+T_SENSOR+"')")
    print("Se agrego un nuevo registro")
    connection.commit()
connection.close()
