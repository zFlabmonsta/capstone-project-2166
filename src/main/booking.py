from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from main.models import Dashboard, Property, Location, Booking
from .forms import Property_form
from geopy.geocoders import Nominatim

from datetime import datetime, date, time

"""
To make booking we need to get the property the user wants to book. To this the will search for
property that are available, filtering out (date, location, number of guest)
"""
@login_required(login_url='/login')
def make_booking(request, property_id, i_year, i_month, i_day, o_year, o_month, o_day):
    if (request.method == 'POST'):
        current_user = request.user
        check_in = datetime(i_year, i_month, i_day)
        check_out = datetime(o_year, o_month, o_day)
        # create booking object
        d = Dashboard.objects.get(user=current_user.id)
        p = Property.objects.get(id=property_id)
        p.time_booked_incr()
        b = Booking(property=p, dashboard=d, start_date=check_in, end_date=check_out)
        b.save()
        return HttpResponseRedirect('/dashboard')
    return HttpResponseRedirect('/dashboard')

