<?php
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'admin');
define('DB_PASSWORD', '12345');
define('DB_DATABASE', 'MAIN_SERVER');
$link = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);

// Check connection
if($link === false){
   echo "ERROR: No se puede conectar  " ;
	header("Location: /index.html");
}else {
   if($_SERVER["REQUEST_METHOD"] == "POST") {
      $myusername =$_POST['email'];
      $mypassword =$_POST['password'];

      $sql = "SELECT * FROM USUARIOS WHERE Email=MD5('$myusername') AND Password=MD5('$mypassword')";
      echo $sql;
      $result = mysqli_query($link,$sql);
      $count = mysqli_num_rows($result);
      echo $count;
      // If result matched $myusername and $mypassword, table row must be 1 row

      if($count == 1) {
         session_start();
        $_SESSION['email'] = $myusername;
         echo 'Bienvenido'; //<a href="asset/logout.php"> Cerrar sesion </a>;
         header("Location: /dashboard.php");

      }else {
         header("Location: /index.html");
         echo 'Usuario/Password Incorrecto';
      }
  }
 }

?>
