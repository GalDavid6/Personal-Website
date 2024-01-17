from django.urls import path
from . import views


app_name='todolist'
urlpatterns = [
    path('', views.home_todo, name='home_todo'),
    path('delete/<str:pk>', views.delete_todo, name='delete_todo'),
]