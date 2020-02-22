from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


def home(request):
    title = 'Home'
    return render( request, 'home.html', {'title': title})


def about(request):
    title = 'Sobre'
    return render( request, 'about.html', {'title': title})


def contact(request):
    title = 'Contato'
    return render( request, 'contact.html', {'title': title})


def login_logout(request):
    title = 'Wellcome'
    return render( request, 'login_logout_create.html', {'title': title})



def your_booking(request):
    title = 'Suas reservas'
    return render( request, 'your_bookings.html', {'title': title})