import os
import requests

from dotenv import load_dotenv


load_dotenv()

def get_weather_data(city_name):
    data = make_weather_api_call(city_name)  
    weather_data = {
        'city': f"{data['name']}, {data['sys']['country']}",
        'weather_now': f"{data['weather'][0]['main']}, {data['weather'][0]['description']}",
        'temperature': round(data['main']['temp']),
        'feels_like': round(data['main']['feels_like']),
        'humidity': str(data['main']['humidity'])
    }
    return weather_data

def is_valid_city(request):
    city_name = request.POST['city_name']
    data = make_weather_api_call(city_name)
    if "name" in data:
        request.session['last_searched_city'] = city_name
        return city_name
    else:
        return request.session.get('last_searched_city')

def make_weather_api_call(city_name):
    query_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_options = "units=metric&exclude=minutely,alerts&"
    api_key = "appid=" + os.getenv("WEATHER_API_KEY")
    url = f"{query_url}q={city_name}&{api_options}{api_key}" 
    return requests.get(url).json()
