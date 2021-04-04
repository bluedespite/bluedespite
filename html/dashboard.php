<!doctype html>

<?php
   session_start();

   if(!isset($_SESSION['email'])){
     header("Location: index.html");
     exit;
   }
?>

<html lang="en">
<head>
  <title>Roraima Dashboard</title>
  <link href="asset/css/bootstrap.css" rel="stylesheet">
  <link href="asset/css/bootstrap-utilities.css" rel="stylesheet">

  <style>
  .link-unstyled{text-decoration:none;color:#000000;}
  .toright{text-align: right;}
  .toleft{text-align: left;}
  body{font-size: 18px; font-family: sans-serif;}
  </style>

</head>

  <body >
    <div class="container-fluid" >
      <div class="row ">
        <div class ="my-auto col-2 text-dark bg-white" >
            <a class="link-unstyled " href="dashboard.php">
              <span data-feather="slack"  ></span>
              Roraima Dashboard
            </a>

          </div>
          <div class ="col-4 text-dark bg-white toleft" >
              <a class="link-unstyled text-dark ">
                <img src="asset/logo.JPG" alt="Roraima" class="img-fluid" width="100" height="100"  style="float:left">

              </a>
            </div>
            <div class ="col-6 text-dark bg-white toright my-auto" >
                <a class="link-unstyled text-dark" href="logout.php">
                  <span data-feather="log-out"  ></span>
                  Logout
                </a>
              </div>
      </div>

      <div class="row h-100">
        <div class= "col-2 bg-dark  sidebar-sticky " >
          <a href="#" class="link-unstyled text-white">
          <p>
            <i data-feather="slack"></i>
            Dashboard
          </p>
          </a>
          <a href="#" class="link-unstyled text-white">
          <p>
            <i data-feather="slack"></i>
            Dashboard 1
          </p>
          </a>
          <a class="link-unstyled text-light" href="#">
          <p>
            <i data-feather="slack"></i>
            Dashboard 2
          </p>
          </a>
        </div>
        <div class= "col-10 bg-white text-dark" >
          <p>  Grafico de Tendencia</p>
          <canvas id="miGrafico"></canvas>
        </div>
      </div>
    </div>

    <script crossorigin="anonymous" integrity="sha384-xBuQ/xzmlsLoJpyjoggmTEz8OWUFM0/RC5BsqQBDX2v5cMvDHcMakNTNrHIW2I5f" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script crossorigin="anonymous" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script crossorigin="anonymous" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <script src="asset/js/jquery-3.2.1.slim.min.js" ></script>
    <script src="asset/js/core/popper.min.js"></script>
    <script src="asset/js/core/bootstrap.min.js"></script>
    <script src="asset/js/feather.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.js" integrity="sha256-JG6hsuMjFnQ2spWq0UiaDRJBaarzhFbUxiUTxQDA9Lk=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.min.js" integrity="sha256-XF29CBwU1MWLaGEnsELogU6Y6rcc5nCkhhx89nFMIDQ=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.js" integrity="sha256-J2sc79NPV/osLcIpzL3K8uJyAD7T5gaEFKlLDM18oxY=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js" integrity="sha256-CfcERD4Ov4+lKbWbYqXD6aFM9M51gN4GUEtDhkWABMo=" crossorigin="anonymous"></script>
     <script type="text/javascript" src="js/datos.js"></script> 
  </body>
</html>
