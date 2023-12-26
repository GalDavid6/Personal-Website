from django.shortcuts import render
import json
import requests


# Create your views here.
def weather(request):
    if request.method == 'POST':
        city= request.POST['city']
        source = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3dbe4a2f24971f881442c2c974dd61a6"
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

