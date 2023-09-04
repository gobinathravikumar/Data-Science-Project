import requests
import streamlit as st


st.set_page_config(page_title='WEATHER DATA REPORT', page_icon=":umbrella_with_rain_drops:", layout="wide")
st.header("Welcome to WEATHER API :umbrella_with_rain_drops:")
st.title('Weather forecasts in a fast and elegant way')
API_KEY = "273d54f85d535a237f38055afdb4058a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather_data(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        st.error("Failed to retrieve weather data.")
        return None

def format_as_json(weather_data):
    temperature_fahrenheit = weather_data['main']['temp']
    temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
    formatted_data = {
        "Weather": f"{int(temperature_celsius)} C",
        "Latitude": weather_data['coord']['lat'],
        "Longitude": weather_data['coord']['lon'],
        "City": weather_data['name']
    }
    return formatted_data

def format_as_xml(weather_data):
    xml_data = f"""<?xml version="1.0" encoding="UTF-8"?>
<WeatherData>
    <Weather>{weather_data['main']['temp']} C</Weather>
    <Latitude>{weather_data['coord']['lat']}</Latitude>
    <Longitude>{weather_data['coord']['lon']}</Longitude>
    <City>{weather_data['name']}</City>
</WeatherData>
"""
    return xml_data

CITY = st.text_input('Enter your city name')
st.write('To view the report in JSON format, click here ')
json_format_button = st.button('JSON Format')
st.write('To view the report in XML format, click here ')
xml_format_button = st.button('XML Format')

if json_format_button:
    weather_data = get_weather_data(CITY)
    if weather_data:
        formatted_data = format_as_json(weather_data)
        st.write(formatted_data)

if xml_format_button:
    weather_data = get_weather_data(CITY)
    if weather_data:
        formatted_data = format_as_xml(weather_data)
        st.code(formatted_data, language='xml')
