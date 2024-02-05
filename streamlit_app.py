# Import modules
import requests
import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playergamelog
import streamlit as st

# Define a function to get the average points per game for a player in a season
def get_avg_ppg(player_id, season):
  # Get the game logs for the player in the season
  player_logs = playergamelog.PlayerGameLog(player_id=player_id, season=season)
  player_logs_df = player_logs.get_data_frames()[0]
  # Calculate the average points per game
  avg_ppg = player_logs_df["PTS"].mean()
  return avg_ppg

# Define a function to plot the average points per game for a player over multiple seasons
def plot_avg_ppg(player_id, seasons):
  # Initialize an empty list to store the average points per game
  avg_ppg_list = []
  # Loop through the seasons and get the average points per game
  for season in seasons:
    avg_ppg = get_avg_ppg(player_id, season)
    avg_ppg_list.append(avg_ppg)
  # Plot the average points per game as a line chart
  plt.plot(seasons, avg_ppg_list, marker="o")
  plt.xlabel("Season")
  plt.ylabel("Average Points Per Game")
  plt.title(f"Average Points Per Game for Player ID {player_id}")
  return plt

# Use Streamlit to create a web app
st.title("NBA Stats App")
st.write("This app shows the average points per game for a given player over multiple seasons.")

# Create a sidebar to select the player ID and the seasons
st.sidebar.header("Select the player and the seasons")
player_id = st.sidebar.number_input("Enter the player ID (e.g. 2544 for LeBron James)", min_value=1, max_value=9999, value=2544)
seasons = st.sidebar.multiselect("Select the seasons", ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"], default=["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"])

# Plot the average points per game for the selected player and seasons
fig = plot_avg_ppg(player_id, seasons)
st.pyplot(fig)
