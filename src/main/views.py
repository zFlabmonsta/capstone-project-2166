from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from main.models import Dashboard, Property, Location
from .forms import Property_form

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
    properties = Property.objects.filter(dashboard__id = dashboard.id)
    return render(request, "main/dashboard.html", {"properties": properties})

"""
loads up a form where the user then enters in the form to fill out so that the user can
list the property for accommodation
"""
@login_required(login_url='/login')
def create_property(request):
    current_user = request.user
    if request.method == 'POST':
        form = Property_form(request.POST)
        if form.is_valid():
            # Enter property info on dashboard
            street = form.cleaned_data['street']
            post_code = form.cleaned_data['post_code']
            suburb = form.cleaned_data['suburb']
            # Change this to make it user specific
            d = Dashboard.objects.get(user=current_user.id)

            l = Location(street=street, post_code=post_code, suburb=suburb)
            l.save()
            p = Property(dashboard = d, location = l)
            p.save()
            return HttpResponseRedirect('/dashboard')
    else:
        form = Property_form()
    return render(request, "main/property_form.html", {'form':form})

"""
deletes the property from the database
"""
@login_required(login_url='/login')
def delete_property(request, id):
    if request.method == 'POST':
        # delete property
        Property.objects.get(id=id).delete()
        # get current user to redirect to dashboard
        current_user = request.user
        dashboard_id = Dashboard.objects.get(user=current_user.id).id
    return HttpResponseRedirect('/dashboard')
