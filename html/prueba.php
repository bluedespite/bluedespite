<?php
// Seteamos la cabecera a JSON

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

$query=sprintf("SHOW TABLES");
$result = $mysqli->query($query);
echo $result;
$query = sprintf("SELECT ID, FECHA_HORA, LVL_PROD, LVL_WTR,tmp FROM Torrix_MEASURE");
echo $result;


$result = $mysqli->query($query);

// Hacemos un bucle con los datos obntenidos
$data = array();
foreach ($result as $row) {
	$data[] = $row;
}

// Limpiamos memoria consumida al extraer los datos
$result->close();

// Cerramos la conexión a la Base de Datos
$mysqli->close();
?>
