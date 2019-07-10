from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from main.models import Dashboard, Property, Location
from .forms import Property_form, Search_property_form

# Create your views here.

# Home Page
def index(request):
    search_form = Search_property_form()
    return render(request, "main/index.html", {'search_form': search_form})

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
    properties = Property.objects.filter(dashboard__id = dashboard.id)
    return render(request, "main/dashboard.html", {"properties": properties})

