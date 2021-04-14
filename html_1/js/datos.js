$(document).ready(function() {
    $.ajax({
        url: "php/datos.php",
        dataType: 'json',
        contentType: "application/json; charset=utf-8",
        method: "GET",
        success: function(data) {
            var FECHA_HORA = [];
            var LVL_PROD = [];
            var LVL_WTR= [];
            var tmp= [];
            var color = ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)', 'rgba(255, 159, 64, 0.2)'];
            var bordercolor = ['rgba(255,99,132,1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'];
            console.log(data);

            for (var i in data) {
                FECHA_HORA.push(data[i].FECHA_HORA);
                LVL_PROD.push(data[i].LVL_PROD);
                LVL_WTR.push(data[i].LVL_WTR);
                tmp.push(data[i].tmp);
            }

            var chartdata = {
                labels: FECHA_HORA,
                datasets: [
                {   label: 'Producto',
                    data: LVL_PROD,
                    borderColor: color[0],
                    backgroundColor: color[0],
                    yAxisID: 'A'
                    
                },
                {   label: 'Temperatura',
                    data: tmp,
                    borderColor: color[1],
                    backgroundColor: color[1],
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
        error: function(data) {
            console.log(data);
        }
    });
});
