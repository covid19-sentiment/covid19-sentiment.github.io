function createMap(){
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var myObj = JSON.parse(this.responseText);
    // console.log(myObj)
    var election = new Datamap({
        scope: 'usa',
        element: document.getElementById('map'),
        geographyConfig: {
          highlightBorderColor: '#bada55',
         popupTemplate: function(geography, data) {
            return '<div class="hoverinfo">' + geography.properties.name + ' Sentiment:' +  data.Sentiment_value + ' '
          },
          highlightBorderWidth: 3
        },
        // tutorial for filling a map with a graditent of colors https://www.youtube.com/watch?v=_sqqxcRf9hw
        fills: {
        'Republican': '#CC4731',
        'Democrat': '#306596',
        'Heavy Democrat': '#667FAF',
        'Light Democrat': '#A9C0DE',
        'Heavy Republican': '#CA5E5B',
        'Light Republican': '#EAA9A8',
        '0.1': '#CCFFCC',
        '0.2': '#CCFFCC',
        '0.3': '#99FF99',
        '0.4': '#99FF99',
        '0.5': '#66FF66',
        '0.6': '#66FF66',
        '0.7': '#33FF33',
        '0.8': '#33FF33',
        '0.9': '#00FF00',
        '1.0': '#00FF00',
        '0': '#FFFFCC',
        '-0.1': '#FFCCCC',
        '-0.2': '#FFCCCC',
        '-0.3': '#FF9999',
        '-0.4': '#FF9999',
        '-0.5': '#FF6666',
        '-0.6': '#FF6666',
        '-0.7': '#FF3333',
        '-0.8': '#FF3333',
        '-0.9': '#FF0000',
        '-1.0': '#FF0000',
        defaultFill: '#FFFFFF'
      },
      data:myObj
      });
      election.labels();
  }
};
xmlhttp.open("GET", "https://raw.githubusercontent.com/covid19-sentiment/covid19-sentiment.github.io/master/state_sentiment_example.json", true);
xmlhttp.send();
}
