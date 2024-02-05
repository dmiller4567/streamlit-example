# Import the required modules
import requests
import pandas as pd
import streamlit as st

# Define the base URL for the NBA API
base_url = "https://stats.nba.com/stats/"

# Define the endpoint for the daily leaders
endpoint = "leagueleaders"

# Define the parameters for the request
params = {
    "LeagueID": "A", # NBA
    "PerMode": "PerGame", # Per game stats
    "Scope": "S", # Season
    "Season": "2023-24", # Current season
    "SeasonType": "Regular Season", # Regular season
    "StatCategory": "PTS" # Points
}

# Define the headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer": "https://stats.nba.com/leaders/",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true"
}

# Make the request and get the response
response = requests.get(base_url + endpoint, params=params, headers=headers)

# Check the status code
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Get the column names
    columns = data["resultSet"]["headers"]

    # Get the row values
    rows = data["resultSet"]["rowSet"]

    # Create a pandas dataframe
    df = pd.DataFrame(rows, columns=columns)

    # Display the dataframe using streamlit
    st.title("NBA Daily Stats App")
    st.write("This app shows the top 50 players in points per game for the current season.")
    st.dataframe(df)
else:
    # Display an error message
    st.error("Could not fetch the data from the NBA API. Please try again later.")
