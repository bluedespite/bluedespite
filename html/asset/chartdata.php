<?php
session_start();

if(!isset($_SESSION['email'])){
  header("Location: /index.html");
  exit;
}

define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'admin');
define('DB_PASSWORD', '12345');
define('DB_DATABASE', 'MAIN');
$link = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);

if($link === false){
  die("conection failed")
   header("Location: /index.html");
}

$sql = "SELECT * FROM TORRIX ORDER BY ID DESC";
echo $sql;


//sql statement to run
$sql = "SELECT formStatus, COUNT(formStatus) AS total FROM studentForm GROUP BY formStatus;";

//run sql query and store into variable
$result = mysqli_query($conn,$sql);
$data = array();

foreach ($result as $row) {
 $data[] = $row;
}

//free memory and close db connection
$result->close();
$conn->close();

// IMPORTANT, output to json
echo json_encode($data);

?>
