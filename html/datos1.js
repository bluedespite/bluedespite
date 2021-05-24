$(document).ready(function() {
    $.ajax({
        url: "data1.php",
        dataType: 'json',
        contentType: "application/json; charset=utf-8",
        method: "GET",
        success: function(data) {
            var FECHA_HORA = [];
            var LVL1 = [];
            var LVLWTR= [];
            var TMP= [];
            var LAT=[];
            var LON=[];
            var VEL=[];
            var TRYC[];
            var color = ['rgba(255, 0, 0, 0.2)', 'rgba(0, 0, 153, 0.2)', 'rgba(0, 102, 0, 0.2)', 'rgba(255, 255, 0, 0.2)', 'rgba(255, 102, 0, 0.2)', 'rgba(102, 0, 153, 0.2)', 'rgba(102, 0, 0, 0.2)'];
            var bordercolor = ['rgba(255,0,0,1)', 'rgba(0, 0, 153, 1)', 'rgba(0, 102, 0, 1)', 'rgba(255, 255, 0, 1)', 'rgba(255, 102, 0, 1)', 'rgba(102, 0, 153, 1)', 'rgba(0, 0, 0, 1)'];
            console.log(data);

            for (var i in data) {
                FECHA_HORA.push(data[i].FECHA_HORA);
                LVL1.push(data[i].LVL1);
                LVLWTR.push(data[i].LVLWTR);
                TMP.push(data[i].TMP);
                LAT.push(data[i].LAT);
                LON.push(data[i].LON);
                VEL.push(data[i].VEL);
                TRYC[0].push([data[i].LAT);
                TRYC[1].push([data[i].LON);
            }
            console.log("value,", TRYC);
            var chartdata = {
                labels: FECHA_HORA,
                datasets: [
                {   label: 'Producto',
                    data: LVL1,
                    borderColor: color[0],
                    backgroundColor: color[0],
                    yAxisID: 'A'

                },
                {   label: 'Nivel Agua',
                    data: LVLWTR,
                    borderColor: color[1],
                    backgroundColor: color[1],
                    yAxisID: 'A'

                },
                {   label: 'Velocidad',
                    data: VEL,
                    borderColor: color[2],
                    backgroundColor: color[2],
                    yAxisID: 'A'

                },
                {   label: 'Temperatura',
                    data: TMP,
                    borderColor: color[3],
                    backgroundColor: color[3],
                    yAxisID: 'B'
                }]};

            var mostrar = $("#miGrafico");

            var grafico = new Chart(mostrar, {
                type: 'line',
                data: chartdata,
                options: {
                    responsive: true,
                    scales: {
                        yAxes: [
                        {id:'A',ticks: {min: 0,max: 100}},
                        {id:'B',ticks: {min: 0,max: 100}}

                            ]
                    }
                }
            });
        },
        error: function(data1) {
        console.log(data1);
        }
    });
});
