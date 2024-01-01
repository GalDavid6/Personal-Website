from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


# Create your views here.
def home(request):
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        content= request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, " Please fill out the form as required")
        else:
            contact= Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, " Your message has been sent")
    return render(request, 'home.html')



