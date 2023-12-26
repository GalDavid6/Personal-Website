from django.urls import path
from . import views

app_name='todolist'
urlpatterns = [
    path('', views.add_todo, name='add_todo'),
    path('delete/<str:pk>', views.delete, name='delete')
]