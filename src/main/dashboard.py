from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from main.models import Dashboard, Property, Location, Booking, image, Property_review
from .forms import Property_form, Review_form
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
            

            print(form.cleaned_data['free_parking'])

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
                    apartment = form.cleaned_data['apartment'],
                    hotel = form.cleaned_data['hotel'],
                    house = form.cleaned_data['house'],
                    resort = form.cleaned_data['resort'],
                    townhouse = form.cleaned_data['townhouse'],
                    # amenities
                    kitchen = form.cleaned_data['kitchen'],
                    airconditioning = form.cleaned_data['airconditioning'],
                    bathroom = form.cleaned_data['bathroom'],
                    tv = form.cleaned_data['tv']
                )
            p.save()

            # create image models and save them to db
            first_image = False 
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

@login_required(login_url='/login')
def give_review(request, id):
    current_user = request.user
    dashboard_id = Dashboard.objects.get(user=current_user.id).id
    booking = Booking.objects.get(id=id)
    review_form = Review_form()
    context = {
        "form": review_form,
    }
    if (request.method == 'POST'):
        form = Review_form(request.POST)
        if form.is_valid():
            _review = form.cleaned_data['review']
            _rating = form.cleaned_data['rating']
            obj = Property_review(property=booking.property, review=_review, rating=_rating)
            obj.save()
            return HttpResponseRedirect('/dashboard')

    if (booking.dashboard.id == dashboard_id):
        return render(request, "main/give_review.html", context)
    return HttpResponseRedirect('/dashboard')

def moreinfo(request, which, id):
    if (which == 'p'):
        property = Property.objects.get(id=id)
        booking = None
    elif (which == 'b'):
        booking = Booking.objects.get(id=id)
        property = Property.objects.get(id=booking.property.id)
    images = image.objects.filter(property__id=property.id)
    reviews = Property_review.objects.filter(property__id=property.id)

    context = {
        'which': which,
        'property': property,
        'booking': booking,
        'images': images,
        'reviews':reviews
    }
    return render(request, "main/moreinfo.html", context)
     


