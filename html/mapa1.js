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
            var PFINAL=[data[i].LAT,data[i].LON];
            console.log(data);
            for (var i in data) {
                FECHA_HORA.push(data[i].FECHA_HORA);
                LVL1.push(data[i].LVL1);
                VEL.push(data[i].VEL);
                TRYC.push([data[i].LAT,data[i].LON]);
            }
            console.log("value,", i);
            console.log("value,", TRYC);
            var mymap = L.map('mapid').setView(PFINAL, 13);
          	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
          		maxZoom: 18,
          		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
          			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          		id: 'mapbox/streets-v11',
          		tileSize: 512,
          		zoomOffset: -1
          	}).addTo(mymap);

          	L.marker(PFINAL).addTo(mymap).bindPopup("<b>Ubicacion Final</b><br/>").openPopup();
      	     L.polygon(TRYC).addTo(mymap).bindPopup("Trayectoria Recorrida");
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
