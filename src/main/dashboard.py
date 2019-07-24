from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from main.models import Dashboard, Property, Location, Booking, image
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
        form = Property_form(request.POST, request.FILES)
        if form.is_valid():
            # Change this to make it user specific
            d = Dashboard.objects.get(user=current_user.id)

            # Enter property info on dashboard
            num = form.cleaned_data['num']
            street = form.cleaned_data['street']
            post_code = form.cleaned_data['post_code']
            suburb = form.cleaned_data['suburb']
            price = form.cleaned_data['price']
            num_guests = form.cleaned_data['num_guests']
            num_rooms = form.cleaned_data['num_rooms']
            desc = form.cleaned_data['description']

            # get full address, longitude and latitude 
            geo_location = Nominatim(timeout=3)
            geo_location = geo_location.geocode(str(num)+" "+street+" "
                    +suburb+" "+str(post_code), "NSW")
            full_address = str(geo_location.address)
            longitude = float(geo_location.longitude)
            latitude = float(geo_location.latitude)

            l = Location(num=num, address=full_address, longitude=longitude, latitude=latitude)
            l.save()

            p = Property(dashboard = d, location = l, price=price, num_guests=num_guests, 
                    num_rooms=num_rooms, description=desc, 
                    display_image=request.FILES.getlist('image')[0])
            p.save()

            # create image models and save them to db
            for f in request.FILES.getlist('image'):
                img = image(property=p, image=f)
                img.save()

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
        Property.objects.get(id=id).delete()
        current_user = request.user
        dashboard_id = Dashboard.objects.get(user=current_user.id).id
    return HttpResponseRedirect('/dashboard')


"""
delete booking from the database
"""
@login_required(login_url='/login')
def delete_booking(request, id):
    if request.method =='POST':
        Booking.objects.get(id=id).delete()
        current_user = request.user
        dashboard_id = Dashboard.objects.get(user=current_user.id).id
    return HttpResponseRedirect('/dashboard')
