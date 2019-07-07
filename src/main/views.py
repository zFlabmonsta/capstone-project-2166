from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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
    Redirect add class button to create class to dashboard [x]
NOTE:
    Currently load dashboard(id=1)
"""
@login_required(login_url='/login')
def dashboard(response, id):
    dashboard = get_object_or_404(Dashboard, id=id)
    classes = MyClass.objects.filter(dashboard__id = id)
    return render(response, "main/dashboard.html", {"classes":classes})

"""
This method allows the user to fill in a form to create a class holding 
the evaluated learning outcomes, then redirect the user to the dashboard
once the form is completed succesfully
"""
@login_required(login_url='/login')
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
            return HttpResponseRedirect('/dashboard')
    else:
        form = Class_form()
    return render(response, "main/class_form.html", {'form':form})

"""
When this method is called, the class, given the id, will be removed from the database.
Once pressed it will redirect the user to the dashboard
"""
@login_required(login_url='/login')
def delete_class(response, id):
    if response.method == 'POST':
        MyClass.objects.get(id=id).delete()
    return HttpResponseRedirect('/dashboard')
