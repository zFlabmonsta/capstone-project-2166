from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
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
direct the user to their dashboard
"""
@login_required(login_url='/login')
def dashboard(request):
    current_user = request.user
    dashboard = Dashboard.objects.get(user=current_user.id)
    classes = MyClass.objects.filter(dashboard__id = dashboard.id)
    return render(request, "main/dashboard.html", {"classes":classes})

"""
This method allows the user to fill in a form to create a class holding 
the evaluated learning outcomes, then redirect the user to the dashboard
once the form is completed succesfully
"""
@login_required(login_url='/login')
def create_class(request):
    current_user = request.user
    if request.method == 'POST':
        form = Class_form(request.POST)
        if form.is_valid():
            # Enter Class into dashboard
            course_code = form.cleaned_data['course_code']
            # Change this to make it user specific
            d = Dashboard.objects.get(user=current_user.id)
            c = MyClass(dashboard = d, class_name = course_code)
            c.save()
            return HttpResponseRedirect('/dashboard')
    else:
        form = Class_form()
    return render(request, "main/class_form.html", {'form':form})

"""
When this method is called, the class, given the id, will be removed from the database.
Once pressed it will redirect the user to the dashboard
"""
@login_required(login_url='/login')
def delete_class(request, id):
    if request.method == 'POST':
        # delete class
        MyClass.objects.get(id=id).delete()
        # get current user to redirect to dashboard
        current_user = request.user
        dashboard_id = Dashboard.objects.get(user=current_user.id).id
    return HttpResponseRedirect('/dashboard')
