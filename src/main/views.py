from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home Page
def index(response):
    return HttpResponse("<h1>Home Page!</h1>")

def about(response):
    return HttpResponse("<h1> About! </h1>")

def dashboard(response):
    return HttpResponse("<h1> Dashboard! </h1>")

def howto(response):
    return HttpResponse("<h1> Howto !</h1>")
