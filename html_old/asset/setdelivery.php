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

// Check connection
if($link === false){
   header("Location: /index.html");
}else {
   if($_SERVER["REQUEST_METHOD"] == "POST") {

      $fechasf =$_POST['fecha'];
      $fecha=date('Y-m-d H:i:s',strtotime($fechasf));
      $guia =$_POST['guia'];
      $producto =$_POST['producto'];
      $cantidad =$_POST['cantidad'];
      $punit=$_POST['punit'];
      $tfact =$_POST['tfact'];
      $um =$_POST['um'];
      $proveedor =$_POST['proveedor'];
      $estacion =$_POST['estacion'];
      $tanque =$_POST['tanque'];
      $comentarios =$_POST['comentarios'];

      $sql = "SELECT ID FROM DELIVERIES ORDER BY ID DESC LIMIT 1";
      echo $sql;
      $result = mysqli_query($link,$sql);
      $count = mysqli_num_rows($result);
      $row=mysqli_fetch_array($result,MYSQLI_NUM);
      if ($count == 1) {
      $lastid = $row[0] +1;
      }else {
      $lastid = 1;
      }
      $sql = "INSERT INTO DELIVERIES (ID, FECHA, GUIA, PRODUCTO, PRECIO_UNITARIO, CANTIDAD, UM, TFACTURA, PROVEEDOR, ESTACION, TANQUE, COMENTARIOS) VALUES ('$lastid', '$fecha', '$guia', '$producto', '$punit', '$cantidad', '$um', '$tfact', '$proveedor', '$estacion', '$tanque', '$comentarios')";
      echo $sql;
      $result = mysqli_query($link,$sql);
      header("Location: /deliveries.php");


  }
 }

?>
