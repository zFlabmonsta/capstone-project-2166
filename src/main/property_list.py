from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

from main.models import Dashboard, Property, Location, Booking, image 
from .forms import Property_form

from geopy.geocoders import Nominatim

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
            try: 
                geo_location = Nominatim(timeout=10)
                geo_location = geo_location.geocode(str(num)+" "+street+" "
                        +suburb+" "+str(post_code), "NSW")
                longitude = float(geo_location.longitude)
                latitude = float(geo_location.latitude)
            except AttributeError: 
                messages.error(request, "Cannot find location, try again")
                return HttpResponseRedirect('/create_property')


            l = Location(num=num, street=street, post_code=post_code, suburb=suburb, longitude=longitude, latitude=latitude)
            l.save()
            
            p = Property(dashboard = d, 
                    location = l, 
                    price=price, 
                    num_guests=num_guests, 
                    num_rooms=num_rooms, 
                    description=desc, 
                    free_parking=form.cleaned_data['free_parking'],
                    pool = form.cleaned_data['pool'],
                    gym = form.cleaned_data['gym'],
                    spa = form.cleaned_data['spa'],
                    ramp = form.cleaned_data['ramp'],
                    travelator = form.cleaned_data['travelator'],
                    elevator = form.cleaned_data['elevator'],
                    # property Type
                    property_type = form.cleaned_data['property_type'],
                    # amenities
                    kitchen = form.cleaned_data['kitchen'],
                    airconditioning = form.cleaned_data['airconditioning'],
                    bathroom = form.cleaned_data['bathroom'],
                    tv = form.cleaned_data['tv']
                )
            p.save()

            # create image models and save them to db
            for f in request.FILES.getlist('image'):
                img = image(property=p, image=f)
                img.save()

            return HttpResponseRedirect('/dashboard')
    else:
        form = Property_form()
    return render(request, "main/property_form.html", {'form':form})

@login_required(login_url='/login')
def edit_property_listing(request, id):
    instance = get_object_or_404(Property, id=id)
    form = Property_form()
    imgs = image.objects.filter(property__id=id)
    context = {
        'images':imgs,
        'form': form,
        'obj': instance
    }

    if (request.method == 'POST'):
        form = Property_form(request.POST, request.FILES)
        if form.is_valid():
            property = Property.objects.get(id=id)
            property.location.num = form.cleaned_data['num']
            property.location.street = form.cleaned_data['street']
            property.location.suburb = form.cleaned_data['suburb']
            property.location.post_code = form.cleaned_data['post_code']
            property.price= form.cleaned_data['price']
            property.num_guests= form.cleaned_data['num_guests']
            property.num_rooms= form.cleaned_data['num_rooms']
            property.description= form.cleaned_data['description']
            property.free_parking=form.cleaned_data['free_parking']
            property.pool = form.cleaned_data['pool']
            property.gym = form.cleaned_data['gym']
            property.spa = form.cleaned_data['spa']
            property.ramp = form.cleaned_data['ramp']
            property.travelator = form.cleaned_data['travelator']
            property.elevator = form.cleaned_data['elevator']
                # property Type
            property.property_type= form.cleaned_data['property_type']
                # amenities
            property.kitchen = form.cleaned_data['kitchen']
            property.airconditioning = form.cleaned_data['airconditioning']
            property.bathroom = form.cleaned_data['bathroom']
            property.tv = form.cleaned_data['tv']
            property.wifi = form.cleaned_data['wifi']
            property.laundry = form.cleaned_data['laundry']
            property.save()

            for f in request.FILES.getlist('image'):
                img = image(property=instance, image=f)
                img.save()
            return HttpResponseRedirect('/dashboard')
    
    return render(request, "main/edit_property_form.html", context)

@login_required(login_url='/login')
def delete_property(request, id):
    if request.method == 'POST':
        Property.objects.get(id=id).delete()
        current_user = request.user
        dashboard_id = Dashboard.objects.get(user=current_user.id).id
    return HttpResponseRedirect('/dashboard')
