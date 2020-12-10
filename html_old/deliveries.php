
<?php
   session_start();

   if(!isset($_SESSION['email'])){
     header("Location: index.html");
     exit;
   }


?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <link rel="apple-touch-icon" sizes="76x76" href="asset/img/apple-icon.png">
  <link rel="icon" type="image/png" href="asset/img/favicon.png">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <title>
    Roraima Bussiness Integrated
  </title>
  <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no' name='viewport' />
  <!--     Fonts and icons     -->
  <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700,200" rel="stylesheet" />
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <!-- CSS Files -->
  <link href="asset/css/bootstrap.min.css" rel="stylesheet" />
  <link href="asset/css/now-ui-dashboard.css?v=1.5.0" rel="stylesheet" />
  <!-- CSS Just for demo purpose, don't include it in your project -->
  <link href="/asset/demo/demo.css" rel="stylesheet" />
</head>

<body class="">
  <div class="wrapper ">
    <div class="sidebar" data-color="blue">
      <div class="logo">
        <a href="#" class="simple-text logo-mini">
          RBI
        </a>
        <a href="#" class="simple-text logo-normal">
          Roraima <br>
          Bussiness Integrated
        </a>
      </div>
      <div class="sidebar-wrapper" id="sidebar-wrapper">
        <ul class="nav">
          <li >
            <a href="dashboard.php">
              <i class="now-ui-icons design_app"></i>
              <p>Dashboard</p>
            </a>
          </li>
          <li>
            <a href="Inventario.php">
              <i class="now-ui-icons business_chart-bar-32"></i>
              <p>inventario</p>
            </a>
          </li>
          <li class="active ">
            <a href="deliveries.php">
              <i class="now-ui-icons shopping_delivery-fast"></i>
              <p>Deliveries</p>
            </a>
          </li>
          <li>
            <a href="Ajustes.php">
              <i class="now-ui-icons design-2_ruler-pencil"></i>
              <p>Ajustes de Inventario</p>
            </a>
          </li>
          <li>
            <a href="sales.php">
              <i class="now-ui-icons business_money-coins"></i>
              <p>Sales</p>
            </a>
          </li>
          <li>
            <a href="Reporte.php">
              <i class="now-ui-icons files_single-copy-04"></i>
              <p>Reportes</p>
            </a>
          </li>
          <li>
            <a href="Notificaciones.php">
              <i class="now-ui-icons ui-1_bell-53"></i>
              <p>Notificaciones</p>
            </a>
          </li>
          <li class="active-pro">
            <a href="Ajustes.php">
              <i class="now-ui-icons ui-1_settings-gear-63"></i>
              <p>Ajustes</p>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="main-panel" id="main-panel">
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-transparent  bg-primary  navbar-absolute">
        <div class="container-fluid">
          <div class="navbar-wrapper">
            <div class="navbar-toggle">
              <button type="button" class="navbar-toggler">
                <span class="navbar-toggler-bar bar1"></span>
                <span class="navbar-toggler-bar bar2"></span>
                <span class="navbar-toggler-bar bar3"></span>
              </button>
            </div>
            <a class="navbar-brand" href="#pablo">Dashboard</a>
          </div>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navigation" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-bar navbar-kebab"></span>
            <span class="navbar-toggler-bar navbar-kebab"></span>
            <span class="navbar-toggler-bar navbar-kebab"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-end" id="navigation">
            <form>
              <div class="input-group no-border">
                <input type="text" value="" class="form-control" placeholder="Search...">
                <div class="input-group-append">
                  <div class="input-group-text">
                    <i class="now-ui-icons ui-1_zoom-bold"></i>
                  </div>
                </div>
              </div>
            </form>
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link" href="#pablo">
                  <i class="now-ui-icons media-2_sound-wave"></i>
                  <p>
                    <span class="d-lg-none d-md-block">Stats</span>
                  </p>
                </a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="now-ui-icons location_world"></i>
                  <p>
                    <span class="d-lg-none d-md-block">Some Actions</span>
                  </p>
                </a>
                <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownMenuLink">
                  <a class="dropdown-item" href="#">Action</a>
                  <a class="dropdown-item" href="#">Another action</a>
                  <a class="dropdown-item" href="#">Something else here</a>
                </div>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#pablo">
                  <i class="now-ui-icons users_single-02"></i>
                  <p>
                    <span class="d-lg-none d-md-block">Account</span>
                  </p>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <!-- End Navbar -->
      <div class="panel-header panel-header-sm">
      </div>
      <div class="content">
        <div class="row">
          <div class="col-md">


            <div class="card">
              <div class="card-header">
                <h4 class="card-title"> Insert Manual Delivery</h4>
              </div>
              <div class="card-body">
                <form class="form-signin" action="asset/setdelivery.php" method="post">
                  <div class="row">
                    <div class="col-md-4 pr-1">
                      <div class="form-group">
                        <label>Fecha</label>
                        <input type="datetime-local" name="fecha" class="form-control" placeholder="Fecha" required>
                      </div>
                    </div>
                    <div class="col-md-4 px-1">
                      <div class="form-group">
                        <label>Guia</label>
                        <input type="text" class="form-control" name="guia" placeholder="Guia" required >
                      </div>
                    </div>

                    <div class= "col-md-4 pl-1">
                      <div class= "form-group">
                        <label>Producto</label>
                        <select class="browser-default custom-select" name="producto">
                          <option selected>Open this...</option>
                          <option value="DB5S50">Diesel DB5S50</option>
                          <option value="GASOHOL95">Gasohol 95</option>
                          <option value="GASOHOL90">Gasohol 90</option>
                        </select>
                        </div>
                      </div>
                    </div>

                    <div class="row">
                      <div class="col-md-4 pr-1">
                        <div class="form-group">
                          <label>Proveedor</label>
                          <input type="text" class="form-control" placeholder="Proveedor" name="proveedor" required>
                        </div>
                      </div>



                      <div class="col-md-4 px-1">
                        <div class="form-group">
                          <label>Estacion</label>
                            <select class="browser-default custom-select" name="estacion">
                              <option selected>Open this...</option>

                              <?php
                                define('DB_SERVER', 'localhost');
                                define('DB_USERNAME', 'admin');
                                define('DB_PASSWORD', '12345');
                                define('DB_DATABASE', 'MAIN');
                                $link = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
                                if($link === false){
                                  header("Location: /index.html");
                                  }
                                  else{
                                  $sql = "SELECT DISTINCT EESS FROM ESTACIONES ORDER BY ID DESC";
                                  $result = mysqli_query($link,$sql);
                                  $count = mysqli_num_rows($result);
                                  if ($count >= 1) {
                                    while ($row=mysqli_fetch_array($result,MYSQLI_NUM)){
                                      echo '<option value="' . $row[0] .'">' . $row[0] .'</option>';
                                      }
                                    }}
                                ?>
                          </select>
                        </div>
                      </div>

                      <div class="col-md-4 pl-1">
                        <div class="form-group">

                          <label>Tanque <?php echo $estacion  ?></label>
                            <select class="browser-default custom-select" name="tanque">
                              <option selected>Open this...</option>

                              <?php
                                define('DB_SERVER', 'localhost');
                                define('DB_USERNAME', 'admin');
                                define('DB_PASSWORD', '12345');
                                define('DB_DATABASE', 'MAIN');
                                $link = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
                                if($link === false){
                                  header("Location: /index.html");
                                  }
                                  else{
                                  $sql = "SELECT DISTINCT EESS FROM ESTACIONES ORDER BY ID DESC";
                                  $result = mysqli_query($link,$sql);
                                  $count = mysqli_num_rows($result);
                                  if ($count >= 1) {
                                    while ($row=mysqli_fetch_array($result,MYSQLI_NUM)){
                                      echo '<option value="' . $row[0] .'">' . $row[0] .'</option>';
                                      }
                                    }}
                                ?>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="row">
                      <div class="col-sm">
                        <div class="form-group">
                          <label>Cantidad</label>
                          <input type="text" class="form-control" placeholder="Galones" name="cantidad" required>
                        </div>
                      </div>

                      <div class="col-sm ">
                        <div class="form-group">
                          <label>Precio Unit</label>
                          <input type="text" class="form-control" placeholder="Precio Unit" name="punit" required>
                        </div>
                      </div>

                      <div class="col-sm ">
                        <div class="form-group">
                          <label>Total Factura</label>
                          <input type="text" class="form-control" placeholder="Total" name="tfact" required>
                        </div>
                      </div>

                      <div class= "col-sm ">
                        <div class= "form-group">
                          <label>UM</label>
                          <select class="browser-default custom-select" name="um">
                            <option selected>Open this...</option>
                            <option value="Gallons">Galones</option>
                            <option value="Liters">Litros</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="row">
                      <div class="col-sm">
                        <div class="form-group">
                          <label>Comentarios</label>
                          <input type="text" class="form-control" placeholder="Comentarios" name="comentarios" value=" " required>
                        </div>
                      </div>
                    </div>
                    <button class="btn btn-sm btn-primary " type="submit">Insert Delivery</button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>


      <div class="content">
        <div class="row">
          <div class="col-md">
            <div class="card">
              <div class="card-header">
                <h4 class="card-title"> Last Deliveries</h4>
                </div>
                <div class="card-body">
                  <div class="table-responsive-sm">
                    <table class="table table-sm table-bordered">
                      <thead class="text-primary text-sm">
                        <tr>
                          <td>Fecha</td>
                          <td>Guia</td>
                          <td>Producto</td>
                          <td>PUnit</td>
                          <td>Cantidad</td>
                          <td>UM</td>
                          <td>Total</td>
                          <td>Proveedor</td>
                          <td>Estacion</td>
                          <td>Tanque</td>
                          <td>Comentarios</td>
                        </tr>
                      </thead>
                      <tbody>

                  <?php
                    define('DB_SERVER', 'localhost');
                    define('DB_USERNAME', 'admin');
                    define('DB_PASSWORD', '12345');
                    define('DB_DATABASE', 'MAIN');
                    $link = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);

                    // Check connection
                    if($link === false){
                      header("Location: /index.html");
                      }
                      else{
                      $sql = "SELECT * FROM DELIVERIES ORDER BY ID DESC LIMIT 50";
                      $result = mysqli_query($link,$sql);
                      $count = mysqli_num_rows($result);
                      if ($count > 1) {
                        echo "<tr>";
                        while ($row=mysqli_fetch_array($result,MYSQLI_NUM)){
                          for ($i=0;$i<11;$i++){
                          echo "<td>";
                          echo $i;
                          echo $row[$i+1];
                          echo "</td>";
                        }
                        echo "</tr>";
                      }
                    }}
                   ?>
                 </tr>
                  </tbody>
                </table>
              </div>

              </div>
            </div>
          </div>
        </div>
      </div>


    </div>






  <!--   Core JS Files   -->
  <script src="asset/js/core/jquery.min.js"></script>
  <script src="asset/js/core/popper.min.js"></script>
  <script src="asset/js/core/bootstrap.min.js"></script>
  <script src="asset/js/plugins/perfect-scrollbar.jquery.min.js"></script>
  <!--  Google Maps Plugin    -->
  <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY_HERE"></script>
  <!-- Chart JS -->
  <script src="asset/js/plugins/chartjs.min.js"></script>
  <!--  Notifications Plugin    -->
  <script src="asset/js/plugins/bootstrap-notify.js"></script>
  <!-- Control Center for Now Ui Dashboard: parallax effects, scripts for the example pages etc -->
  <script src="asset/js/now-ui-dashboard.min.js?v=1.5.0" type="text/javascript"></script><!-- Now Ui Dashboard DEMO methods, don't include it in your project! -->
  <script src="asset/demo/demo.js"></script>


</body>

</html>
