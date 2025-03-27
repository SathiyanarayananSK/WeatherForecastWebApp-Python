import requests
import streamlit as st
import os

# OpenWeatherMap API key
API_KEY = st.secrets["general"]["WeatherAPIKey"]

def get_data(place, days):
    """Fetch weather forecast data for a given place and number of days."""
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]
    nr_values = 8 * days  # Each day has 8 data points (3-hour intervals)
    filtered_data = filtered_data[:nr_values]  # Limit data to the requested number of days
    return filtered_data

if __name__ == "__main__":
    # Test the function with Tokyo and 3 days of forecast
    fd = get_data(place="Tokyo", days=3)
    dates = [dic["dt_txt"] for dic in fd]  # Extract dates from the filtered data
    print(dates)
