from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Dashboard, MyClass
from .forms import Class_form

# Create your views here.

# Home Page
def index(response):
    return render(response, "main/index.html", {})

def about(response):
    return HttpResponse("<h1> About! </h1>")

def howto(response):
    return HttpResponse("<h1> Howto !</h1>")

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

def create_class(response):
    if response.method == 'POST':
        form = Class_form(response.POST)
        if form.is_valid():
            # Enter Class into dashboard
            course_code = form.cleaned_data['course_code']
            # Change this to make it user specific
            d = Dashboard.objects.get(id=1)
            c = MyClass(dashboard = d, class_name = course_code)
            c.save()
            return HttpResponseRedirect('dashboard')
    else:
        form = Class_form()
    return render(response, "main/class_form.html", {'form':form})
