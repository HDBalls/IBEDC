// Themes begin
am4core.useTheme(am4themes_animated);
// Themes end

// Create chart instance
var chart = am4core.create("chartdiv", am4charts.PieChart);  

// Add data
chart.data = [ {
  "country": "Meters installed",
  "litres": 525.9,
  "color": am4core.color("#6771dc")
}, {
  "country": "Pending Installation",
  "litres": 110.9,
  "color": am4core.color("#67b7dc")
}, {
  "country": "New requests",
  "litres": 50.1,
  "color": am4core.color("#dc67ce")
}];

// Set inner radius
chart.innerRadius = am4core.percent(60);

//Add label
var label = chart.seriesContainer.createChild(am4core.Label);
label.text = "";
label.horizontalCenter = "middle";
label.verticalCenter = "middle";
      //  label.fontSize = 50;

// Add and configure Series
var pieSeries = chart.series.push(new am4charts.PieSeries());
pieSeries.dataFields.value = "litres";
pieSeries.dataFields.category = "country";
pieSeries.slices.template.stroke = am4core.color("#fff");
pieSeries.slices.template.strokeWidth = 2;
pieSeries.slices.template.propertyFields.fill = "color";
pieSeries.slices.template.strokeOpacity = 1;
pieSeries.ticks.template.disabled = true;
pieSeries.labels.template.disabled = true;

// This creates initial animation
pieSeries.hiddenState.properties.opacity = 1;
pieSeries.hiddenState.properties.endAngle = -90;
pieSeries.hiddenState.properties.startAngle = -90;
$('g:has(> g[aria-labelledby="id-66-title"])').hide();

(function($) { 
  $(function() { 

    //  open and close nav 
    $('#navbar-toggle').click(function() {
      $('nav ul').slideToggle();
    });

    // Hamburger toggle
    $('#navbar-toggle').on('click', function() {
      this.classList.toggle('active');
    });

    // If a link has a dropdown, add sub menu toggle.
    $('nav ul li a:not(:only-child)').click(function(e) {
      $(this).siblings('.navbar-dropdown').slideToggle("slow");

      // Close dropdown when select another dropdown
      $('.navbar-dropdown').not($(this).siblings()).hide("slow");
      e.stopPropagation();
    });


    // Click outside the dropdown will remove the dropdown class
    $('html').click(function() {
      $('.navbar-dropdown').hide();
    });
  }); 
})(jQuery); 