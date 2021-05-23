<?php
// Seteamos la cabecera a JSON
header('Content-Type: application/json');

// Configuramos la conexión a la base de datos
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'admin');
define('DB_PASSWORD', '12345');
define('DB_NAME', 'MAIN_SERVER');

// Desplegamos la conexión a la Basde de Datos
$mysqli = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME);
$mysqli->query("SET NAMES 'utf8'");

if(!$mysqli){
	die("La Conexión ha fallado: " . $mysqli->error);
}
$data = array();
$result = $mysqli->query($query);
$query = sprintf("SELECT ID, FECHA_HORA, LAT, LON,LVL1 ,LVLWTR,TMP FROM tk1_MEASURE");
$result = $mysqli->query($query);

foreach ($result as $row) {
	$data[] = $row;
}

// Limpiamos memoria consumida al extraer los datos
$result->close();

// Cerramos la conexión a la Base de Datos
$mysqli->close();

// Mostramos los datos en formato JSON
print json_encode($data);

//var_dump($data);
