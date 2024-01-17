from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name= 'dashboard'
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_form, name='contact_form'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)