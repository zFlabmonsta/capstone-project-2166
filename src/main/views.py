from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from main.models import Dashboard, Property, Location, Booking
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
            num_room = form.cleaned_data['num_rooms']
            
            # get the longitude and latitude of the where
            where_geolocator = Nominatim(timeout=20)
            where_geolocator = where_geolocator.geocode(where + " " + "NSW, AU")
            where_lat_long = (where_geolocator.latitude, where_geolocator.longitude)

            # find property that is within 5km radius of "where" and list it
            # make query to get list of properties
            list_property = Property.objects.all()
            searching = []
            for property in list_property:
                max_radius = 2000
                property_lat_long = (property.location.latitude, property.location.longitude)
                # add the property if within 5km radius 
                if (geodesic(where_lat_long, property_lat_long).meters < max_radius):
                    searching.append(property)

            # get all properties that are booked in given date
            bookings = Booking.objects.all()
            booked_properties = []
            for b in bookings:
                if (b.date_overlapping(check_in, check_out)):
                   booked_properties.append(b.property.id) 

            # remove property from list, if already booked at given date
            for b in booked_properties:
                for p in searching:
                    if (p.id == b):
                        searching.remove(p)

            # remove property from list, if number of rooms doesnt match
            for p in searching:
                if (not p.is_matching_num_rooms(num_room)):
                    searching.remove(p)

            # remove property from list, if number of guests is less than num_guest
            for p in searching:
                if (not p.is_more_than_guests(num_guest)):
                    searching.remove(p)

            context = {
                'searched_property': searching,
                'start_date': check_in,
                'end_date': check_out,
                'search_property_form': form,
            }

            return render(request, "main/search_list.html", context)

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
    bookings = Booking.objects.filter(dashboard__id=dashboard.id)
    context = {
        'properties': properties,
        'bookings': bookings
    }
    return render(request, "main/dashboard.html", {"properties":properties, "bookings":bookings})

