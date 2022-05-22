am4core.useTheme(am4themes_animated);
// Create chart instance
var chart = am4core.create("chartdiv-line", am4charts.XYChart);
chart.paddingRight = 20;

// Add data
chart.data = [{
  "date": new Date(2018, 3, 20),
  "value": 90,
  "value2": 45
}, {
  "date": new Date(2018, 3, 21),
  "value": 102,
  "value2": 90
}, {
  "date": new Date(2018, 3, 22)
}, {
  "date": new Date(2018, 3, 23),
  "value": 125
}, {
  "date": new Date(2018, 3, 24),
  "value": 55,
  "value2": 90
}, {
  "date": new Date(2018, 3, 25),
  "value": 81,
  "value2": 60
}, {
  "date": new Date(2018, 3, 26)
}, {
  "date": new Date(2018, 3, 27),
  "value": 63,
  "value2": 87
}, {
  "date": new Date(2018, 3, 28),
  "value": 113,
  "value2": 62
}];

// Create axes
var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
dateAxis.renderer.minGridDistance = 50;
dateAxis.renderer.grid.template.strokeWidth = 0;
dateAxis.renderer.grid.template.location = 0.5;
dateAxis.startLocation = 0.5;
dateAxis.endLocation = 0.5;

// Create value axis
var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

// Create series
var series1 = chart.series.push(new am4charts.LineSeries());
series1.dataFields.valueY = "value";
series1.dataFields.dateX = "date";
series1.strokeWidth = 3;
series1.tensionX = 0.8;
series1.bullets.push(new am4charts.CircleBullet());
series1.connect = false;

var series2 = chart.series.push(new am4charts.LineSeries());
series2.dataFields.valueY = "value2";
series2.dataFields.dateX = "date";
series2.strokeWidth = 3;
series2.tensionX = 0.8;
series2.bullets.push(new am4charts.CircleBullet());
