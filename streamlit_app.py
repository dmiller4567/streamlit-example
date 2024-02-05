<html>
<head>
  <!-- Load the Google Charts library -->
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script type="text/javascript">
    // Load the corechart package
    google.charts.load('current', {'packages':['corechart']});
    // Set a callback function to run when the Google Visualization API is loaded
    google.charts.setOnLoadCallback(drawChart);
    // Define the callback function that creates and draws the chart
    function drawChart() {
      // Create a new DataTable object
      var data = new google.visualization.DataTable();
      // Add two columns to the DataTable, one for the player name and one for the points per game
      data.addColumn('string', 'Player');
      data.addColumn('number', 'Points per game');
      // Use an XMLHttpRequest object to fetch the data from the NBA API
      var xhr = new XMLHttpRequest();
      // Set the request URL to the endpoint that returns the player stats for the 2023-24 season
      var url = "https://stats.nba.com/stats/leaguedashplayerstats?Season=2023-24&SeasonType=Regular+Season&MeasureType=Base&PerMode=PerGame&PlusMinus=N&PaceAdjust=N&Rank=N&LeagueID=00&PORound=0&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&TeamID=0&Conference=&Division=&GameSegment=&Period=0&ShotClockRange=&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&DraftYear=&DraftPick=&College=&Country=&Height=&Weight=&api_key=YOUR_API_KEY";
      // Open the request
      xhr.open("GET", url, true);
      // Set the response type to JSON
      xhr.responseType = "json";
      // Set a function to run when the request is completed
      xhr.onload = function() {
        // Check if the status code is 200 (OK)
        if (xhr.status == 200) {
          // Get the response data as a JSON object
          var response = xhr.response;
          // Get the array of player stats from the response object
          var playerStats = response.resultSets[0].rowSet;
          // Sort the array by the points per game in descending order
          playerStats.sort(function(a, b) {
            return b[29] - a[29];
          });
          // Loop through the first 10 elements of the sorted array
          for (var i = 0; i < 10; i++) {
            // Get the player name and the points per game from the current element
            var playerName = playerStats[i][1];
            var pointsPerGame = playerStats[i][29];
            // Add a new row to the DataTable with the player name and the points per game
            data.addRow([playerName, pointsPerGame]);
          }
          // Set some options for the chart, such as the title, the width, the height, and the colors
          var options = {
            title: 'Points per game of the top 10 players in the 2023-24 season',
            width: 800,
            height: 600,
            colors: ['#FF0000', '#0000FF']
          };
          // Create a new BarChart object and pass it the HTML element where the chart will be drawn
          var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
          // Draw the chart with the data and the options
          chart.draw(data, options);
        }
      };
      // Send the request
      xhr.send();
    }
  </script>
</head>
<body>
  <!-- Create a div element where the chart will be drawn -->
  <div id="chart_div"></div>
</body>
</html>
