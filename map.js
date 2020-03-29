// function createMap(){
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
      //   fills: {
      //   '0.1': '#CCFFCC',
      //   '0.2': '#CCFFCC',
      //   '0.3': '#99FF99',
      //   '0.4': '#99FF99',
      //   '0.5': '#66FF66',
      //   '0.6': '#66FF66',
      //   '0.7': '#33FF33',
      //   '0.8': '#33FF33',
      //   '0.9': '#00FF00',
      //   '1.0': '#00FF00',
      //   '0.0': '#FFFFCC',
      //   '-0.1': '#FFCCCC',
      //   '-0.2': '#FFCCCC',
      //   '-0.3': '#FF9999',
      //   '-0.4': '#FF9999',
      //   '-0.5': '#FF6666',
      //   '-0.6': '#FF6666',
      //   '-0.7': '#FF3333',
      //   '-0.8': '#FF3333',
      //   '-0.9': '#FF0000',
      //   '-1.0': '#FF0000',
      //   defaultFill: '#FFFFFF'
      // },
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


      var sentiment_1 = new Datamap({
        scope: 'usa',
        element: document.getElementById('map_1'),
        geographyConfig: {
          highlightBorderColor: '#bada55',
         popupTemplate: function(geography, data) {
            return '<div class="hoverinfo">' + geography.properties.name + ' Sentiment:' +  data.sentimentVal + ' '
          },
          highlightBorderWidth: 3
        },
        // tutorial for filling a map with a graditent of colors https://www.youtube.com/watch?v=_sqqxcRf9hw
      //   fills: {
      //   '0.1': '#CCFFCC',
      //   '0.2': '#CCFFCC',
      //   '0.3': '#99FF99',
      //   '0.4': '#99FF99',
      //   '0.5': '#66FF66',
      //   '0.6': '#66FF66',
      //   '0.7': '#33FF33',
      //   '0.8': '#33FF33',
      //   '0.9': '#00FF00',
      //   '1.0': '#00FF00',
      //   '0.0': '#FFFFCC',
      //   '-0.1': '#FFCCCC',
      //   '-0.2': '#FFCCCC',
      //   '-0.3': '#FF9999',
      //   '-0.4': '#FF9999',
      //   '-0.5': '#FF6666',
      //   '-0.6': '#FF6666',
      //   '-0.7': '#FF3333',
      //   '-0.8': '#FF3333',
      //   '-0.9': '#FF0000',
      //   '-1.0': '#FF0000',
      //   defaultFill: '#FFFFFF'
      // },
      fills:{
        'strong positive':'#F280AA',
        'weak positive':'#F2C4D0',
        "neutral":'#F2E0C9',
        "weak negative":'#8DF2F2',
        "strong negative":'#77C7D9',
        defaultFill: '#FFFFFF'
      },
      data:dataObj
      });
      sentiment_1.labels();
  }
};

xmlhttp.open("GET", "https://raw.githubusercontent.com/covid19-sentiment/covid19-sentiment.github.io/master/state_sentiment_example3.json", true);
xmlhttp.send();
// }
