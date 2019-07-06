from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home Page
def index(response):
    return render(response, "main/index.html", {})

def about(response):
    return HttpResponse("<h1> About! </h1>")

"""
TODO:
    Display Dashboard's Classes [ ]
    Link Dashboard to Registered User [ ]
    Redirect add class button to create class to dashboard [ ]
"""
def dashboard(response):
    return render(response, "main/dashboard.html", {})

def howto(response):
    return HttpResponse("<h1> Howto !</h1>")
