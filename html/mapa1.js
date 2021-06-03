$(document).ready(function() {
    $.ajax({
        url: "data1.php",
        dataType: 'json',
        contentType: "application/json; charset=utf-8",
        method: "GET",
        success: function(data) {
            var TRYC=[];
            var FECHA_HORA=[];
            var LVL1=[];
            var VEL=[];
            var PFINAL=[];
            var Vmax=0;
            var Vmin=300;
            console.log(data);
            for (var i in data) {
                FECHA_HORA.push(data[i].FECHA_HORA);
                LVL1.push(data[i].LVL1);
                VEL.push(data[i].VEL);
                TRYC.push([data[i].LAT,data[i].LON]);
                PFINAL=[data[i].LAT,data[i].LON];
                if (data[i].VEL>Vmax){
                  Vmax=data[i].VEL;
                }
                if (data[i].VEL<Vmin){
                  Vmin=data[i].VEL;
                }}
            console.log(Vmax);
            console.log(Vmin);
            var mymap = L.map('mapid').setView(PFINAL, 13);
          	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
          		maxZoom: 18,
          		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
          			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          		id: 'mapbox/streets-v11',
          		tileSize: 512,
          		zoomOffset: -1
          	}).addTo(mymap);
            var distance = mymap.distance(TRYC[0] ,PFINAL);
            L.marker(TRYC[0]).addTo(mymap).bindPopup("Comienzo");
          	L.marker(PFINAL).addTo(mymap).bindPopup("Final");
      	    L.polyline(TRYC).addTo(mymap).bindPopup("<b>Trayectoria:</b><br> Distancia: "+distance.toString()+ " metros <br> Vel(Max): "+Vmax.toString()+ " Km/h" + "<br> Vel(Min): "+Vmin.toString()+ " Km/h");
          	var popup = L.popup();

          	function onMapClick(e) {
          		popup
          			.setLatLng(e.latlng)
          			.setContent("You clicked the map at " + e.latlng.toString())
          			.openOn(mymap);
          	}
          	mymap.on('click', onMapClick);
          },
          error: function(data1) {
          console.log(data1);
          }
      });
      });
