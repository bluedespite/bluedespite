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
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <link rel="icon" href="../../../../favicon.ico">


    <title>Roraima Dashboard</title>

    <!-- Bootstrap core CSS -->
    <link href="asset/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="dashboard.css" rel="stylesheet">
  </head>


    <nav class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0">
      <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="#">Roraima BI</a>
      <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
      <ul class="navbar-nav px-3">
        <li class="nav-item text-nowrap">
          <a class="nav-link" href="asset/logout.php#">Sign out</a>
        </li>
      </ul>
    </nav>

        <!-- navbar links -->
        <div class="collapse navbar-collapse"
                id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <a class="nav-item nav-link
                    active" href="#">Home</a>
                <a class="nav-item nav-link"
                    href="#">Features</a>
                <a class="nav-item nav-link"
                    href="#">Price</a>
                <a class="nav-item nav-link"
                    href="#">About</a>
            </div>
        </div>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <nav class="col-md-2 d-none d-md-block bg-light sidebar">
          <div class="sidebar-sticky">
            <ul class="nav flex-column">
              <li class="nav-item">
                <a class="nav-link active" href="#">
                  <!--span data-feather="home"></span-->
                  Dashboard <span class="sr-only">(current)</span>
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <!--span data-feather="file"></span-->
                  Orders
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <!--span data-feather="shopping-cart"></span-->
                  Products
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <!--span data-feather="users"></span-->
                  Customers
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <!--span data-feather="bar-chart-2"></span-->
                  Reports
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <!--span data-feather="layers"></span-->
                  Integrations
                </a>
              </li>
            </ul>




</body>

<script src="asset/js/jquery-3.2.1.slim.min.js" ></script>

<script>window.jQuery || document.write('<script src="asset/js/core/jquery-slim.min.js"><\/script>')</script>
<script src="asset/js/core/popper.min.js"></script>
<script src="asset/js/core/bootstrap.min.js"></script>

<!-- Icons -->
<!--script src="https://unpkg.com/feather-icons/dist/feather.min.js"></script-->
<script src="asset/js/feather.min.js"></script>

<script>
  feather.replace()
</script>

<!-- Graphs -->
<script src="asset/js/plugins/chartjs.min.js"></script>

    <script>
      var ctx = document.getElementById("myChart");
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
          datasets: [{
            data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#007bff',
            borderWidth: 4,
            pointBackgroundColor: '#007bff'
          }]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: false
              }
            }]
          },
          legend: {
            display: false,
          }
        }
      });
    </script>
  </body>
</html>
