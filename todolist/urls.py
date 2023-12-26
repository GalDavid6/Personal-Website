from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_todo, name='add'),
    path('delete/<str:pk>', views.delete, name='delete')
]