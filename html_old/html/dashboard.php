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
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <script src="https://unpkg.com/feather-icons"></script>
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@1,800&display=swap" rel="stylesheet">

  <style>
  .link-unstyled{text-decoration:none;color:#000000;}
  .toright{text-align: right;}
  .toleft{text-align: left;}
  </style>

</head>

  <body>
    <div class="wrapper" >
      <div class="wrapper">
		<div class ="col-2 bg-dark sidebar-sticky" >
            <a class="link-unstyled text-light">
				<h4>
				<span data-feather="cloud"  ></span> 
				Roraima </h4>    
            </a>
            <a href="#" class="link-unstyled text-light">
				<h6>
				<span data-feather="codesandbox"></span>
				Resumen </h6>
			</a>
			<a href="#" class="link-unstyled text-light">
				<h6>
				<span data-feather="codepen"></span>
				Reporte</h6> 
			</a>
			<a class="link-unstyled text-light" href="#">
				<h6>
				<span data-feather="user"></span>
				Gestion de Usuarios</h6> 
			</a>
			<a class="link-unstyled text-light" href="#">
				<h6>
				<span data-feather="log-out"></span>
				Salir</h6> 
			</a>
        </div>
        <div class ="col-10 text-dark bg-white" >
              <a class="link-unstyled text-dark toleft" href="#">
              <h4>
              <img src="asset/logo.JPG" alt="Roraima" class="img-fluid" width="100" height="100">
              Resumen de Stocks
              </h4>
			  </a>
            
          <h6>  Resumen de Stock  </h6>
          <canvas id="miGrafico"></canvas>
        </div>
            
      </div>
	  </div>
      
    <script crossorigin="anonymous" integrity="sha384-xBuQ/xzmlsLoJpyjoggmTEz8OWUFM0/RC5BsqQBDX2v5cMvDHcMakNTNrHIW2I5f" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script crossorigin="anonymous" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script crossorigin="anonymous" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.js" integrity="sha256-JG6hsuMjFnQ2spWq0UiaDRJBaarzhFbUxiUTxQDA9Lk=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.min.js" integrity="sha256-XF29CBwU1MWLaGEnsELogU6Y6rcc5nCkhhx89nFMIDQ=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.js" integrity="sha256-J2sc79NPV/osLcIpzL3K8uJyAD7T5gaEFKlLDM18oxY=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js" integrity="sha256-CfcERD4Ov4+lKbWbYqXD6aFM9M51gN4GUEtDhkWABMo=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="js/datos.js"></script> 
    <script>
    feather.replace()
    </script> 
  </body>
</html>
