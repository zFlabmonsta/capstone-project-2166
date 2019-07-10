from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from main.models import Dashboard, Property, Location
from .forms import Property_form
from geopy.geocoders import Nominatim

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
            num = form.cleaned_data['num']
            street = form.cleaned_data['street']
            post_code = form.cleaned_data['post_code']
            suburb = form.cleaned_data['suburb']
            # Change this to make it user specific
            d = Dashboard.objects.get(user=current_user.id)

            # get full address, longitude and latitude 
            geo_location = Nominatim(user_agent=str(current_user.username) + "property")
            geo_location = geo_location.geocode(str(num) + " "+ street + " " + suburb + " " + str(post_code))
            full_address = str(geo_location.address)
            longitude = float(geo_location.longitude)
            latitude = float(geo_location.latitude)
            l = Location(num=num, address=full_address, longitude=longitude, latitude=latitude)
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

"""
To make booking we need to get the property the user wants to book. To this the will search for
property that are available, filtering out (date, location, number of guest)
"""
@login_required(login_url='/login')
def make_booking(request):
    pass
