from django.shortcuts import render
from django.http import HttpResponse
from main.models import Dashboard, MyClass

# Create your views here.

# Home Page
def index(response):
    return render(response, "main/index.html", {})

def about(response):
    return HttpResponse("<h1> About! </h1>")

"""
TODO:
    Display Dashboard's Classes [x]
    Link Dashboard to Registered User [ ]
    Redirect add class button to create class to dashboard [ ]
NOTE:
    Currently load dashboard(id=1)
"""
def dashboard(response):
    classes = MyClass.objects.filter(dashboard__id = 1)
    return render(response, "main/dashboard.html", {"classes":classes})

def howto(response):
    return HttpResponse("<h1> Howto !</h1>")
