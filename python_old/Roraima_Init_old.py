#Se debe e crear la primera vez la Base de datos MAIN_SENSOR mediante el phpmyadmin
#se debe instalar el mysql CONECTOR pip3 install mysql-connector-python
#descomentar los codigos de primera vez que se usa:
import mysql.connector
import csv




csv_configuracion=open('CONFIGURACION.csv')
csv_data=csv.reader(csv_configuracion, delimiter=';')
reg=next(csv_data)
reg=next(csv_data)
#Crear Tabla con nombre tag_CONFIGi
TAG_SENSOR=reg[1]
connection=mysql.connector.connect (host='localhost',database='MAIN_SENSOR',user='admin',password='12345')
cursor=connection.cursor()

sql_select_Query= "CREATE OR REPLACE TABLE `MAIN` ( `ID` INT NOT NULL , `DB_SENSOR` TEXT NOT NULL , INDEX `ID` (`ID`)) ENGINE = InnoDB"
#ATENCION!!!: SOLO USAR LA SIGUIENTE LINEA LA PRIMERA VEZ QUE SE CARGA UN SENSOR, LA SEGUNDA VEZ HAY QUE COMENTAR
cursor.execute(sql_select_Query)

sql_select_Query= "CREATE OR REPLACE TABLE `MAIN_SENSOR`.`"+ TAG_SENSOR + "_CONF` ( `ID` INT NOT NULL , `PARAMETRO` TEXT NOT NULL , `VALOR` TEXT NOT NULL , `DESCRIPCION` TEXT NOT NULL , INDEX `ID` (`ID`)) ENGINE = InnoDB"
cursor.execute(sql_select_Query)
i=1
index=str(i)

sql_select_Query= "INSERT INTO `"+ TAG_SENSOR + "_CONF` (`ID`, `PARAMETRO`, `VALOR`, `DESCRIPCION`) VALUES ("+ index +",'"+ reg[0] +"','"+ reg[1] +"','"+ reg[2] +"')"
cursor.execute(sql_select_Query)
DATOS_COM=['FECHA_HORA']

for reg in csv_data:
    i=i+1
    index=str(i)
    sql_select_Query= "INSERT INTO `"+ TAG_SENSOR + "_CONF` (`ID`, `PARAMETRO`, `VALOR`, `DESCRIPCION`) VALUES ("+ index +",'"+ reg[0] +"','"+ reg[1] +"','"+ reg[2] +"')"
    cursor.execute(sql_select_Query)
    if i>6:
        DATOS_COM.append(reg[1])

connection.commit()

sql_select_Query= "CREATE OR REPLACE TABLE `MAIN_SENSOR`.`"+ TAG_SENSOR + "_MEASURE` ( `ID` INT NOT NULL ,"

for n in DATOS_COM:
    sql_select_Query= sql_select_Query + "`" + n + "` FLOAT NOT NULL,"

j=len(sql_select_Query)
sql_select_Query=sql_select_Query[:j-1]
sql_select_Query=sql_select_Query + "  , INDEX `ID` (`ID`)) ENGINE = InnoDB"

cursor.execute(sql_select_Query)
cursor.execute("ALTER TABLE `"+TAG_SENSOR+"_MEASURE` CHANGE `FECHA_HORA` `FECHA_HORA` DATETIME NOT NULL");

sql_select_Query = ("SELECT * FROM MAIN " "WHERE DB_SENSOR = '"+TAG_SENSOR+"'")
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
    cursor.execute("INSERT INTO `MAIN` (`ID`,`DB_SENSOR`) VALUES ("+index+",'"+TAG_SENSOR+"')")
    print("Se agrego un nuevo registro")
    connection.commit()

connection.close()
csv_configuracion.close()
