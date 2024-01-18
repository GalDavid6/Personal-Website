from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Todo
from .utils import handle_post_request
from .weather_utils import get_weather_data


# Create your views here.
def delete_todo(request, pk):
    Todo.delete_todo(pk)
    return redirect(reverse('todolist:home_todo'))

def home_todo(request):
    city_name = None
    if request.method == 'POST':
        city_name = handle_post_request(request)

    if city_name == None:
        city_name = request.session.get('last_searched_city', "Tel Aviv")

    all_todos = Todo.get_all_todo()
    weather_data = get_weather_data(city_name)

    data = {
        "city": weather_data['city'],
        'weather_now': weather_data['weather_now'],
        "temperature": weather_data['temperature'],
        "feels_like": weather_data['feels_like'],
        "humidity": weather_data['humidity'],
        "todos": all_todos
    }

    return render(request, 'todolist.html', data)
