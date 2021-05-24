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
            var color = ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)', 'rgba(255, 159, 64, 0.2)'];
            var bordercolor = ['rgba(255,99,132,1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'];
            console.log(data);

            for (var i in data) {
                FECHA_HORA.push(data[i].FECHA_HORA);
                LVL1.push(data[i].LVL1);
                LVLWTR.push(data[i].LVLWTR);
                TMP.push(data[i].TMP);
            }

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
                {   label: 'Temperatura',
                    data: TMP,
                    borderColor: color[2],
                    backgroundColor: color[2],
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
                        {id:'A',ticks: {min: 0,max: 10000}},
                        {id:'B',ticks: {min: 0,max: 1000}}

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
