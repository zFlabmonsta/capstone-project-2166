from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.template import RequestContext
from django.contrib import messages

from main.models import Dashboard, Property, Location, Booking, image, Property_review
from .forms import Property_form, Search_property_form, Filter_facilities, Filter_disability_access, Filter_property_type, Filter_amenities

from .filter_help import *

from datetime import datetime, date, time
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def index(request):
    # forms
    search_form = Search_property_form()
    filter_facilities_form = Filter_facilities()
    disability_access_form = Filter_disability_access()
    property_type_form = Filter_property_type()
    amenities_form = Filter_amenities()

    context = {
        'search_property_form': search_form, 
        'filter_facilities': filter_facilities_form,
        'disability_access_form': disability_access_form,
        'property_type_form': property_type_form,
        'amenities_form': amenities_form
    }

    if (request.method == 'POST'):

        # forms
        form = Search_property_form(request.POST)
        filter_facilities_form = Filter_facilities(request.POST)
        disability_access_form = Filter_disability_access(request.POST)
        property_type_form = Filter_property_type(request.POST)
        amenities_form = Filter_amenities(request.POST)

        if form.is_valid():
            where = form.cleaned_data['where']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            num_guest = form.cleaned_data['num_guests']
            num_room = form.cleaned_data['num_rooms']
            
            # get the longitude and latitude of the where
            try:
                where_geolocator = Nominatim(timeout=20)
                where_geolocator = where_geolocator.geocode(where + " " + "NSW, AU")
                where_lat_long = (where_geolocator.latitude, where_geolocator.longitude)
            except AttributeError:
                messages.error(request, "Cannot find location, try again")
                return HttpResponseRedirect('/')


            searching = []
            # find property that is within 5km radius of "where" and list it
            list_property = Property.objects.all()
            searching = filter_by_distance(list_property, searching, where_lat_long)
            # get all properties that are booked in given date
            bookings = Booking.objects.all()
            searching = filter_by_date(bookings, searching, check_in, check_out)
            # remove property from list, if number of rooms doesnt match
            searching = filter_by_room(num_room, searching)
            # remove property from list, if number of guests is less than num_guest
            searching = filter_by_guest(num_guest, searching)
            searching = filter_by_facilities(filter_facilities_form, searching)
            searching = filter_by_disability_access(disability_access_form, searching)
            searching = filter_by_property_type(property_type_form, searching)
            searching = filter_by_amenities(amenities_form, searching)
           
            # get display images for each property 
            display = get_display_images(searching)
            searching = list(zip(searching, display))

            context = {
                'searched_property': searching,
                'start_date': check_in,
                'end_date': check_out,
                'search_property_form': form,
                'property_type_form': property_type_form,
                'disability_access_form': disability_access_form,
                'filter_facilities': filter_facilities_form,
                'amenities_form': amenities_form,
                'reviews': reviews
            }

            return render(request, "main/search_list.html", context)

    return render(request, "main/index.html", context)

def about(response):
    return HttpResponse("<h1> About! </h1>")

def map(request, lat, lng):
    return render(request, "main/googlemap.html", {"lat":lat, "lng":lng})


def moreinfo(request, which, property_id, i_year, i_month, i_day, o_year, o_month, o_day):
    # get property id 
    check_in = datetime(i_year, i_month, i_day).date
    check_out = datetime(o_year, o_month, o_day).date

    search_property_form = Search_property_form()

    property = Property.objects.get(id=property_id)
    images = image.objects.filter(property__id=property_id)
    reviews = Property_review.objects.filter(property__id=property_id)

    context = {
        'which': which,
        'search_property_form': search_property_form,
        'start_date': check_in,
        'end_date': check_out,
        'property': property,
        'images': images,
        'reviews':reviews
    }
    return render(request, "main/moreinfo.html", context)
     
def handler404(request, exception):
    context = {}
    return render(request, "main/404.html", context)






















