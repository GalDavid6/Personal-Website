from django.shortcuts import render
from decouple import config
import json
import requests


# Create your views here.
def weather(request):
    queryUrl = "https://api.openweathermap.org/data/2.5/weather?q=tel aviv&"
    apiOptions = "units=metric&exclude=minutely,alerts&"
    apiKey = "appid=" + config("WEATHER_API_KEY")
    url = queryUrl + apiOptions + apiKey
    list_of_data = requests.get(url).json()
    data= {
        "Sunrise": str(list_of_data['sys']['sunrise']),
        "Sunset": str(list_of_data['sys']['sunset']),
        "Tempeture": round((list_of_data['main']['temp'])),
        "Feels like": round((list_of_data['main']['feels_like'])),
        "humidity": str(list_of_data['main']['humidity']),            
    }
    return render(request, "weather.html", data)

def weather2(request):
    if request.method == 'POST':
        city= request.POST['city']
        source = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid="
        list_of_data = requests.get(source.format(city)).json()
        data= {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": round((list_of_data['main']['temp']-32)* 5.0/9.0, 2),
            "humidity": str(list_of_data['main']['humidity']),            
        }
    else:
        data= {}
    return render(request, "weather.html", data)

        # // Backgrounds
        # switch (main) {
        # case "Snow":
        # document.getElementById("wrapper-bg").style.backgroundImage =
        # "url('https://mdbgo.io/ascensus/mdb-advanced/img/snow.gif')";
        # break;
        # case "Clouds":
        # document.getElementById("wrapper-bg").style.backgroundImage =
        # "url('https://mdbgo.io/ascensus/mdb-advanced/img/clouds.gif')";
        # break;
        # case "Fog":
        # document.getElementById("wrapper-bg").style.backgroundImage =
        # "url('https://mdbgo.io/ascensus/mdb-advanced/img/fog.gif')";
        # break;
        # case "Rain":
        # document.getElementById("wrapper-bg").style.backgroundImage =
        # "url('https://mdbgo.io/ascensus/mdb-advanced/img/rain.gif')";
        # break;
        # case "Clear":
        # document.getElementById("wrapper-bg").style.backgroundImage =
        # "url('https://mdbgo.io/ascensus/mdb-advanced/img/clear.gif')";
        # break;
        # case "Thunderstorm":
        # document.getElementById("wrapper-bg").style.backgroundImage =
        # "url('https://mdbgo.io/ascensus/mdb-advanced/img/thunderstorm.gif')";
        # break;
        # default:
        # document.getElementById("wrapper-bg").style.backgroundImage =
        # "url('https://mdbgo.io/ascensus/mdb-advanced/img/clear.gif')";
        # break;
        # }