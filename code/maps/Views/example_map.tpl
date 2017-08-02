<head>
    <title>Weather Map</title>
    <style>
       #map {
        width: 100%;
        height: 400px;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>
      function get_icon(temperature) {
        // return 'static/images/marker_blue25.png'
        if (temperature < 22)   
          color = "blue";
        else if (temperature < 24)   
          color = "green";
        else if (temperature < 26)   
          color = "white";
        else if (temperature < 28)   
          color = "yellow";
        else if (temperature < 30)   
          color = "orange";
        else
          color = "red";
        temperature = Math.round(temperature)
        if (temperature < 0) {
          temp = "";
        }
        else if (temperature > 99) {
          temp = "";
        }
        else {
          temp = temperature.toString();
        }
        // return "http://labs.google.com/ridefinder/images/mm_20_" + color + temp + ".png";
        // return "https://raw.githubusercontent.com/Concept211/Google-Maps-Markers/master/images/marker_" + color + temp + ".png"
        return "static/images/marker_" + color + temp + ".png"
      }
      function initMap() {
        var mapDiv = document.getElementById('map');
        var map = new google.maps.Map(mapDiv, {
            center: {lat: 41.150000	, lng: -81.360000},
            zoom: 14
        });
        //var image = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
        var icon_image = "http://labs.google.com/ridefinder/images/mm_20_gray.png"
        var icon_data = {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 10
          }
        %for item in data:
            var location = {lat: {{item['lat']}}, lng: {{item['lon']}}}
            var marker = new google.maps.Marker({
                position: location,
                map : map,
                icon : get_icon({{item['temperature']}}),
                //icon : icon_image,
                title: "{{str(item['temperature'])}}"
            });
        %end
      }
    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB02ukUFZmjBKRzD_DX-Fipb__nFFeUNmU&callback=initMap">
    </script>
  </body>
