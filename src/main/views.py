from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from main.models import Dashboard, Property, Location
from .forms import Property_form, Search_property_form

# Create your views here.

# Home Page
def index(request):
    search_form = Search_property_form()
    if (request.method == 'POST'):
        form = Search_property_form(request.POST)
        if form.is_valid():
            where = form.cleaned_data['where']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            num_guest = form.cleaned_data['num_guests']
            
            # get the longitude and latitude of the where
            where_geolocator = Nominatim(user_agent="")
            where_geolocator = where_geolocator.geocode(where + " " + "NSW, AU")
            where_lat_long = (where_geolocator.latitude, where_geolocator.longitude)

            # find property that is within 5km radius of "where" and list it
            # make query to get list of properties
            list_property = Property.objects.all()
            in_radius = []
            for property in list_property:
                max_radius = 2000
                property_lat_long = (property.location.latitude, property.location.longitude)
                # add the property if within 5km radius 
                if (geodesic(where_lat_long, property_lat_long).meters < max_radius):
                    in_radius.append(property)

           #DEBUG
            for p in in_radius:
                print(p.location.address)
            return render(request, "main/search_list.html", {'searched_property': in_radius})

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

