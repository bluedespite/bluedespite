$(document).ready(function() {
    $.ajax({
        url: "data1.php",
        dataType: 'json',
        contentType: "application/json; charset=utf-8",
        method: "GET",
        success: function(data) {
            var txt1="";
            console.log(data);
            for (var i in data) {
                txt1+="<tr><td>"+data[i].FECHA_HORA.toString()+"</td>";
                txt1+="<td>"+data[i].LAT.toString()+","+data[i].LON.toString()+"</td>";
                txt1+="<td>"+data[i].VEL.toString()+"</td>";
                txt1+="<td>"+data[i].LVL1.toString()+"</td>";
                txt1+="<td>"+data[i].LVLWTR.toString()+"</td>";
                txt1+="<td>"+data[i].TMP.toString()+"</td>";
                txt1+=  "</tr>";
                if (i === 20) { break; }
                }
                var txt = "<thead><tr><th>FECHA HORA</th><th>POSICION</th>";
                txt+="<th>VELOCIDAD (KMPH)</th><th>NIVEL DE PRODUCTO</th><th>NIVEL DE AGUA</th>";
                txt+="<th>TEMPERATURA</th></tr></thead><tbody>";
                txt+=txt1+"<tr></tbody>";
                document.getElementById("tablad").innerHTML=txt;
          },
          error: function(data) {
          console.log(data);
          }
      });
      });
