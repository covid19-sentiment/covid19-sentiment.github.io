var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var dataObj = JSON.parse(this.responseText);
    var sentiment = new Datamap({
        scope: 'usa',
        element: document.getElementById('map'),
        geographyConfig: {
          highlightBorderColor: '#bada55',
         popupTemplate: function(geography, data) {
            return '<div class="hoverinfo">' + geography.properties.name + ' Sentiment:' +  data.sentimentVal + ' '
          },
          highlightBorderWidth: 3
        },
        // tutorial for filling a map with a graditent of colors https://www.youtube.com/watch?v=_sqqxcRf9hw
      fills:{
        'strong positive':'#F2543D',
        'weak positive':'#F28268',
        "neutral":'#EEEEEE',
        "weak negative":'#87EBA8',
        "strong negative":'#38C477',
        defaultFill: '#FFFFFF'
      },
      data:dataObj
      });
      sentiment.labels();
    }
  }
  xmlhttp.open("GET", "https://raw.githubusercontent.com/covid19-sentiment/covid19-sentiment.github.io/master/state_sentiment_example3.json", true);
  xmlhttp.send();

function show_s_map(val) {
  var URL = "" + val + ".json"
  console.log(URL)
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      var dataObj = JSON.parse(this.responseText);
      var sentiment = new Datamap({
        scope: 'usa',
        element: document.getElementById('map'),
        geographyConfig: {
          highlightBorderColor: '#bada55',
          popupTemplate: function (geography, data) {
            return '<div class="hoverinfo">' + geography.properties.name + ' Sentiment:' + data.sentimentVal + ' '
          },
          highlightBorderWidth: 3
        },
        // tutorial for filling a map with a graditent of colors https://www.youtube.com/watch?v=_sqqxcRf9hw
        fills: {
          'strong positive': '#F2543D',
          'weak positive': '#F28268',
          "neutral": '#EEEEEE',
          "weak negative": '#87EBA8',
          "strong negative": '#38C477',
          defaultFill: '#FFFFFF'
        },
        data: dataObj
      });
      sentiment.labels();
    }
  }
  xmlhttp.open("GET", "https://raw.githubusercontent.com/covid19-sentiment/covid19-sentiment.github.io/master/state_sentiment_example3.json", true);
  xmlhttp.send();
}

// var xmlhttp_1 = new XMLHttpRequest();
// xmlhttp_1.onreadystatechange = function() {
//   if (this.readyState == 4 && this.status == 200) {
//     var dataObj = JSON.parse(this.responseText);
//     var sentiment_1 = new Datamap({
//       scope: 'usa',
//       element: document.getElementById('map_1'),
//       geographyConfig: {
//         highlightBorderColor: '#bada55',
//        popupTemplate: function(geography, data) {
//           return '<div class="hoverinfo">' + geography.properties.name + ' Sentiment:' +  data.sentimentVal + ' '
//         },
//         highlightBorderWidth: 3
//       },
//     fills:{
//       'strong positive':'#F280AA',
//       'weak positive':'#F2C4D0',
//       "neutral":'#F2E0C9',
//       "weak negative":'#8DF2F2',
//       "strong negative":'#77C7D9',
//       defaultFill: '#FFFFFF'
//     },
//     data:dataObj
//     });
//     sentiment_1.labels();
//     }
//   }
//   xmlhttp_1.open("GET", "https://raw.githubusercontent.com/covid19-sentiment/covid19-sentiment.github.io/master/state_sentiment_example3.json", true);
//   xmlhttp_1.send();

var xmlhttp_1 = new XMLHttpRequest();
xmlhttp_1.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    var dataObj = JSON.parse(this.responseText);
    console.log(dataObj);
    var new_cases = new Datamap({
      scope: 'usa',
      element: document.getElementById('map_1'),
      geographyConfig: {
        highlightBorderColor: '#bada55',
        popupTemplate: function (geography, data) {
          return '<div class="hoverinfo">' + geography.properties.name + 'New Cases:' + data.newCases + ' '
        },
        highlightBorderWidth: 3
      },
      fills: { //#ed2e38
        'level_0': '#ffe0db',
        'level_1': '#ffc1b8',
        "level_2": '#ffa196',
        "level_3": '#ff8175',
        // "level_3":'#f75d56',
        "level_4": '#ed2e38',
        defaultFill: '#FFFFFF'
      },
      data: dataObj
    });
    new_cases.labels();
  }
}
xmlhttp_1.open("GET", "https://raw.githubusercontent.com/covid19-sentiment/covid19-sentiment.github.io/master/python/data_processing/result/state_new_cases_example_wk1.json", true);
xmlhttp_1.send();


function show_map(val) {
  var URL = "https://raw.githubusercontent.com/covid19-sentiment/covid19-sentiment.github.io/master/python/data_processing/result/state_new_cases_example_wk" + val + ".json"
  console.log(URL)
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      var map_elem = document.getElementById('map_1');
      // map_elem.parentNode.removeChild(map_elem);
      map_elem.innerHTML = ""

      var dataObj = JSON.parse(this.responseText);
      console.log(dataObj)
      var new_cases = new Datamap({
        scope: 'usa',
        element: map_elem,
        geographyConfig: {
          highlightBorderColor: '#bada55',
          popupTemplate: function (geography, data) {
            return '<div class="hoverinfo">' + geography.properties.name + 'New Cases:' + data.newCases + ' '
          },
          highlightBorderWidth: 3
        },
        fills: { //#ed2e38
          'level_0': '#ffe0db',
          'level_1': '#ffc1b8',
          "level_2": '#ffa196',
          "level_3": '#ff8175',
          // "level_3":'#f75d56',
          "level_4": '#ed2e38',
          defaultFill: '#FFFFFF'
        },
        data: dataObj
      });
      new_cases.labels();
    }
  }
  xmlhttp.open("GET", URL, true);
  xmlhttp.send();
}