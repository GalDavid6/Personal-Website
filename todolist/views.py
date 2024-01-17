from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Todo
from .utils import handle_post_request
from .weather_utils import get_weather_data, get_weather_data_default_city


# Create your views here.
def delete_todo(request, pk):
    Todo.delete_todo(pk)
    return redirect(reverse('todolist:home_todo'))

def home_todo(request):
    all_todos = Todo.get_all_todo()
    default_city = "Tel Aviv"
    last_searched_city = request.session.get('last_searched_city', default_city)
    city_name = last_searched_city

    if request.method == 'POST':
        handle_post_request(request)
        last_searched_city = request.session.get('last_searched_city', default_city)
        city_name = last_searched_city

    weather_data = get_weather_data(city_name)

    data = {
        "city": weather_data['city'],
        "temperature": weather_data['temperature'],
        "feels_like": weather_data['feels_like'],
        "humidity": weather_data['humidity'],
        "todos": all_todos
    }

    return render(request, 'todolist.html', data)
