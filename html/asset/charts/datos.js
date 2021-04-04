$(document).ready(function() {
    $.ajax({
        url: "/charts/datos.php",
        dataType: 'json',
        contentType: "application/json; charset=utf-8",
        method: "GET",
        success: function(data) {
            var nombre = [];
            var stock = [];
            var precio= [];
            var color = ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)', 'rgba(255, 159, 64, 0.2)'];
            var bordercolor = ['rgba(255,99,132,1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'];
            console.log(data);

            for (var i in data) {
                nombre.push(data[i].nombre);
                stock.push(data[i].stock);
                precio.push(data[i].precio);
            }

            var chartdata = {
                labels: nombre,
                datasets: [
                {   label: 'nombre 1',
                    data: stock,
                    borderColor: color[0],
                    backgroundColor: color[0],
                    yAxisID: 'A'
                    
                },
                {   label: 'nombre 2',
                    data: precio,
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
                        {id:'A',ticks: {min: 0,max: 100}},
                        {id:'B',ticks: {min: 0,max: 10}}
                            
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
