<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Temperature', 'Humidity'],
        %for item in data:
        [ {{item['temperature']}},{{item['humidity']}} ],
        %end
    ]);

    var options = {
        title: 'Temperature vs. Humidity comparison',
        hAxis: {title: 'Temperature', minValue: 0, maxValue: 40},
        vAxis: {title: 'Humidity', minValue: 0, maxValue: 100},
        legend: 'none'
    };

    var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

    chart.draw(data, options);
    }
</script>
</head>
<body>
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
</body>
