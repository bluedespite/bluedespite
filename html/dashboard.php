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
  <link href="dashboard.css" rel="stylesheet">
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
          <canvas id="line-chart" width="400" height="200"></canvas>
        </div>
      </div>
    </div>


    <script src="asset/js/jquery-3.2.1.slim.min.js" ></script>
    <script>window.jQuery || document.write('<script src="asset/js/core/jquery-slim.min.js"><\/script>')</script>
    <script src="asset/js/core/popper.min.js"></script>
    <script src="asset/js/core/bootstrap.min.js"></script>
    <script src="asset/js/feather.min.js"></script>

    <script>
      feather.replace()
    </script>

    <script src="asset/js/plugins/chartjs.min.js"></script>

<script>
    new Chart(document.getElementById("line-chart"), {
      type: 'line',
      data: {
        labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
        datasets: [{
            data: [86,114,106,106,107,111,133,221,783,2478],
            label: "Africa",
            borderColor: "#3e95cd",
            exportEnabled:true,
            animationEnabled:true,
            fill: false
          }, {
            data: [282,350,411,502,635,809,947,1402,3700,5267],
            label: "Asia",
            borderColor: "#8e5ea2",
            fill: false
          }, {
            data: [168,170,178,190,203,276,408,547,675,734],
            label: "Europe",
            borderColor: "#3cba9f",
            fill: false
          }, {
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Latin America",
            borderColor: "#e8c3b9",
            fill: false
          }, {
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "North America",
            borderColor: "#c45850",
            fill: false
          }
        ]
      },
      options: {
        title: {
          display: true,
          text: 'World population per region (in millions)'
        }
      }
    });

</script>


  </body>
</html>
