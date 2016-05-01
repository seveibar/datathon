// Management UI
var rangeSlider = document.getElementById('slider-range');
noUiSlider.create(rangeSlider, {
	start: [ 1996 ],
	range: {
		'min': [ 1995 ],
		'max': [ 2015 ]
	}
});

rangeSlider.noUiSlider.on('update', function( values, handle ) {
  var k = Math.round(values[handle]);
  $('#current-year').html(k);
});

// Map UI
Plotly.d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2010_alcohol_consumption_by_country.csv', function(err, rows){
    function unpack(rows, key) {
        return rows.map(function(row) { return row[key]; });
    }

var data = [{
            type: 'choropleth',
            locationmode: 'country names',
            locations: unpack(rows, 'location'),
            z: unpack(rows, 'alcohol'),
            text: unpack(rows, 'location'),
            autocolorscale: true
        }];

var layout = {
        title: '',
        geo: {
          projection: {
            type: 'robinson'
          }
        },
        width: 960,
        height: 600
    };
    Plotly.plot(map, data, layout, {showLink: false});
    setTimeout(function() {
        var default_value = "USA"
        selectCountry({id: default_value});
        d3.selectAll('path.choroplethlocation')
            .on('click', selectCountry)
            .on('dblclick.zoom', null);
    }, 500);
});

function selectCountry(d) {
  var country = d.id;
  $("#current-country").html(country);
}

// Click Handlers
$('ul.viewing li input').click(function() {
  alert($(this).val());
})
