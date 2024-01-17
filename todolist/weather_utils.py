import os
import requests

from dotenv import load_dotenv


load_dotenv()

def get_weather_data(city_name):
    query_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_options = "units=metric&exclude=minutely,alerts&"
    api_key = "appid=" + os.getenv("WEATHER_API_KEY")
    url = f"{query_url}q={city_name}&{api_options}{api_key}"

    try:
        data = requests.get(url).json()
        if 'name' not in data:
            raise ValueError("Invalid city name")
        
        weather_data = {
            'city': f"{data['name']}, {data['sys']['country']}",
            'weather_now': f"{data['weather']['main']}, {data['weather']['description']}",
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'humidity': str(data['main']['humidity'])
        }

    except (ValueError, requests.RequestException) as e:
        print(f"Error: {e}")
        default_city_data = get_weather_data_default_city()
        weather_data = {
            'city': default_city_data['city'],
            'weather_now': default_city_data['weather_now'],
            'temperature': default_city_data['temperature'],
            'feels_like': default_city_data['feels_like'],
            'humidity': default_city_data['humidity']
        }

    return weather_data

def is_valid_city(city_name):
    query_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_options = "units=metric&exclude=minutely,alerts&"
    api_key = "appid=" + os.getenv("WEATHER_API_KEY")
    url = f"{query_url}q={city_name}&{api_options}{api_key}"

    try:
        data = requests.get(url).json()
        return "name" in data
    except requests.RequestException:
        return False

def get_weather_data_default_city():
    default_url = "http://api.openweathermap.org/data/2.5/weather?q=Tel Aviv&units=metric&exclude=minutely,alerts&appid="
    api_key = os.getenv("WEATHER_API_KEY")
    default_data = requests.get(default_url + api_key).json()

    return {
            'city': f"{default_data['name']}, {default_data['sys']['country']}",
            'weather_now': f"{default_data['weather']['main']}, {default_data['weather']['description']}",
            'temperature': round(default_data['main']['temp']),
            'feels_like': round(default_data['main']['feels_like']),
            'humidity': str(default_data['main']['humidity'])
        }
