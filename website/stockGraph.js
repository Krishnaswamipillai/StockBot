//stockGraph.js
//Author: Harry Hixson
//Project: StockBots
/*
 All CDNs needed for dependencies
<script
src="http://code.jquery.com/jquery-1.12.4.min.js"
integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ="
crossorigin="anonymous">
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/later/1.2.0/later.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.min.js"></script>
*/

//Function for graphing historical data
//Returns reference for changing data on graph
//There must be a graph at elementID for this to work
function graphHD(openP, dateI, elementID, scope){
  var closeP = openP
  
  var today = Date.today()
  
  openP.sort(function(a, b){
        return a[2] - b[2];
  });
  today = new Date(openP[openP.length-1][2])
  var prices = []
  for (x in openP) {
      prices.push(openP[x][0])
  }
  var correctDates = []
  if (datescope == 0){
      targetEpoch = today.addMonths(-1).getDate()
      for (x in openP){
          if (openP[x][2] >= targetEpoch){
              correctDates.push([openP[x][0], openP[x][1]])
          }
      }
  }
  else if (datescope == 1) {
      targetEpoch = today.addMonths(-12).getDate()
      for (x in openP){
          if (openP[x][2] >= targetEpoch){
              correctDates.push([openP[x][0], openP[x][1]])
          }
      }
  }
  else if (datescope == 2) {
      targetEpoch = today.addMonths(-60).getDate()
      for (x in openP){
          if (openP[x][2] >= targetEpoch){
              correctDates.push([openP[x][0], openP[x][1]])
          }
      }
  }
  else if (datescope == 3) {
      //nothing needed -- max scope
  }
    
  console.log(openP)
  openP = correctDates
  closeP = openP
    
  //This function takes in array of stock prices, date of the first
  //price, HTML ID for graph, and the amount of time the graph shows

  //Data that will be passed into the graph
  var graphData = [];
  //Depending on the range of values displayed on graph, only dates
  //at certain intervals will be displayed on x axis (weekly or monthly)
  var graphScope = {month: 'week', year: 'month'};
  //These will be used to determine the date of the given price
  //and if it is a marked opening of closing value
  var priceDate = dateI;
  //initial values for max and min stock price over time period
  //will be used for graph ranges
  var minPrice = Math.min(prices)
  var maxPrice = Math.max(prices)
  //loop to convert data graph
  for (var x = 0; x < openP.length; x++){
    var dayOpen = {
      date: Date.parse(openP[x][1]).getTime(),
      price: openP[x][0]
    };
    //var dayClose = {
    //  date: Date.parse(openP[x][1]).getTime(),
    //  price: closeP[x][0]
    //};

    //Moves formatted data out of loop to use for graph
    graphData.push(dayOpen);
    //graphData.push(dayClose);

    //Changes date if datapoint pushed was market close
    //priceDate.setDate(priceDate.getDate() + 1);

  }

  //Console Log for troubleshooting
  console.log(graphData);
document.getElementById(elementID).innerHTML = ""
  //Creates chart at designated elementID
  var graphRef = new Morris.Line({
    element: elementID,
    data: graphData,
    xkey: 'date',
    ykeys: ['price'],
    labels: ['Price'],
    //ymax: 'auto [maxPrice * 1.1]',
    //ymin: 'auto [minPrice * 0..9]',
    smooth: false,
    hideHover: false,
    parseTime: true,
    preUnits: '$',
    xLabels: graphScope.scope,
    pointSize:0,
    pointStrokeColor:"#29639f",
    fillOpacity: .5
  });
    return graphRef;
}


///////////////////////////////////////////////////////////////////////////////


//Function for graphing real time stock data
//Returns reference for changing data on graph
//Must be existing graph at elementID for this to work
function graphRTD(elementID, prices){
  //Date that will be used for data iteration
  var pointDate = timeI;
  //Creates another 'bounds' to set domain and range of graph
  var rightBound = Date(pointDate.getFullYear(), pointDate.getMonth(), pointDate.getDate(), 16, 00, 0);
  var leftBound = Date(pointDate.getFullYear(), pointDate.getMonth(), pointDate.getDate(), 09, 30, 0);
  var topBound = 0;
  var btmBound = 0;
  //Creates relMax and relMin for calculating top and btm bounds
  var relMax = prices[0];
  var relMin = prices[0];
  //Formatted data that will be used in graph
  var graphData =[];
  //Loop to format data for graph and calculate rightBound
  for (var x = 0; x < prices.length; x++){
    graphData.push({time: pointDate, price: prices[x]});
    //Tests relMax and relMin
    if(relMax < prices[x]){
      relMax = prices[x];
    }
    if(relMin > prices[x]){
      relMin = prices[x];
    }
    pointDate.setMinutes(pointDate.getMinutes() + 1);
  }
  //Calculates values for top & btm bounds
  //values based on relMax and relMin
  topBound = relMax * 1.1;
  btmBound = relMin * .9;


  //Inserts bound points
  graphData.push(
    {time: rightBound, bounds: topBound},
    {time: leftBound,  bounds: btmBound}
  );

  //Function that creates the graph
  var graphRef = Morris.Line({
    element: elementID,
    data: graphData,
    xkey: 'time',
    ykeys: ['price', 'bounds'],
    labels: ['Price', ''],
    ymax: 'auto',
    ymin: 'auto',
    smooth: false,
    hideHover: true,
    parseTime: false,
    preUnits: '$',
    xLabels: "hour",
  });
  return graphRef;
}



//              Schedule works
//later.js schedule for updateGraph Function

//function that creates a schedule for the RT graph to updateGraph
//accounts for different time zones
function schedRT(){
  var offset = new Date().getTimesoneOffset();
  //calculats values for market open and close tome for local time zone
  var openHour = 9 - (offset / 60);
  var openMinute = Math.abs(30 - (offset % 60));
  var closeHour = 16 - (offset / 60);
  var closeMinute = Math.abs((offset % 60));
  if(openHour<0){openHour+= 24;}
  if(closeHour<0){closeHour+= 24;}
  var openTime = openHour + ':' + openMinute;
  var closeTime = closeHour + ':' + closeMinute;
  //creates and returns schedule adjusted to time zone
  var sched = later.parse.recur().on(0).second().after(openTime).time().before(closeTime).time().onWeekday();
  return sched;
}
//var schedRT = later.parse.recur().on(0).second().after('09:30').time().before('16:00').time().onWeekday();
//var minUpdate = later.setInterval(updateGraph, schedRT);






//For RTD graph, function that gets new stock prices
//Triggers minutely
function updateGraph(graphRef, graphData, ticker){
  //Gets time and formats for uniform distribution
  var pointDate = new Date();
  pointDate.setMilliseconds(0);
  pointDate.setSeconds(0);
  //Gets stock data
  //Form here on will be Async
  var minutePrice = 0; //Call to realtime price API using ticker
  graphData.push({time: pointDate, price: minutePrice});
  graphRef.setData(graphData);
}
