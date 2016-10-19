

// Now using `then`
function loadHurricaneMap() {
  var hurricanes = [];

  var min_year = 1950;
  var max_year = 2015;
  return $.getJSON( "/data/result.json", function( data ) {
    var inside = 0;
    var outside = 0;
    $.each( data, function( key, val ) {
        outside ++;
        var year = val['Date']['year'];
        if (year >= min_year && year <= max_year) {
            inside ++;
            hurricane = {};
            hurricane.name = val['name'];
            hurricane.radius = val['Max. Wind Speed'] / 5;
            hurricane.latitude = val['Coordinates']['lat'];
            hurricane.longitude = val['Coordinates']['lon'];
            hurricane.date = val['Date']['year'] + '-' + val['Date']['month'] + '-' + val['Date']['day'];
            hurricane.speed = val['Max. Wind Speed'];
            hurricane.country = 'USA';
            hurricane.fillKey = 'USA';

            hurricanes.push( hurricane );
        }
    });
}).then(function(){
    return hurricanes;
  });
}

//and in your call will listen for the custom deferred's done
loadHurricaneMap().then(function(hurricanes){
    var map = new Datamap({
        scope: 'world',
        element: document.getElementById('container'),
        setProjection: function(element) {
            var projection = d3.geo.equirectangular()
                .center([35, -70])
                .rotate([100 , 0])
                .scale(250)
                .translate([element.offsetWidth / 2, element.offsetHeight / 0.65]);
            var path = d3.geo.path()
                .projection(projection);

            return {path: path, projection: projection};
        },
        // geographyConfig: {
        //     popupOnHover: false,
        //     highlightOnHover: false
        // },
        fills: {
            defaultFill: '#ABDDA4',
            USA: 'blue',
            RUS: 'red'
      }
    });

    map.bubbles(hurricanes, {
      popupTemplate: function(geo, data) {
        return '<div class="hoverinfo">Hurricane ' + data.name + ':<br>' + 'Max wind speed: ' + data.speed + ' kts.<br>  Peaked on ' + data.date + ' near the '  + data.country + '</div>';
      }
    });
});
