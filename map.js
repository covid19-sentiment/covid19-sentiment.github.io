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
            return '<div class="hoverinfo">' + geography.properties.name + ' Sentiment:' +  data.electoralVotes + ' '
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
        defaultFill: '#EDDC4E'
      },
      data:myObj
      });
      election.labels();
  }
};
xmlhttp.open("GET", "https://raw.githubusercontent.com/covid19-sentiment/covid19-sentiment.github.io/master/example.json", true);
xmlhttp.send();
}
