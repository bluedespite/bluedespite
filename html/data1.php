<?php
// Seteamos la cabecera a JSON
header('Content-Type: application/json');

// Configuramos la conexión a la base de datos
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'admin');
define('DB_PASSWORD', '12345');
define('DB_NAME', 'MAIN_SENSOR');

// Desplegamos la conexión a la Basde de Datos
$mysqli = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME);
$mysqli->query("SET NAMES 'utf8'");
$data1 = array();

if(!$mysqli){
	die("La Conexión ha fallado: " . $mysqli->error);
}

// Seleccionamos los datos de la tabla postres
$query = sprintf("SELECT * FROM tk1_MEASURE ORDER BY ID DESC LIMIT 50");
$result = $mysqli->query($query);

// Hacemos un bucle con los datos obntenidos
foreach ($result as $row) {
	$data1[] = $row;
}

// Limpiamos memoria consumida al extraer los datos
$result->close();

// Cerramos la conexión a la Base de Datos
$mysqli->close();

// Mostramos los datos en formato JSON
print json_encode($data1);

//var_dump($data);
?>
