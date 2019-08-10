from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login

from main.models import Dashboard, Property, Location, Booking, image, Property_review
from .forms import Property_form

from .filter_help import get_display_images

@login_required(login_url='/login')
def dashboard(request):
    current_user = request.user
    dashboard = Dashboard.objects.get(user=current_user.id)

    properties = Property.objects.filter(dashboard__id = dashboard.id)
    display = get_display_images(Property.objects.filter(dashboard__id = dashboard.id))
    properties = zip(properties, display)

    bookings = Booking.objects.filter(dashboard__id=dashboard.id)
    display = []
    for b in bookings:
        display.append(b.property)
    display = get_display_images(display)
    bookings = zip(bookings, display)

    context = {
        'properties': properties,
        'bookings': bookings
    }
    return render(request, "main/dashboard.html", context)


@login_required(login_url='/login')
def moreinfo(request, which, id):
    try:
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
    except:
        raise Http404
    return render(request, "main/moreinfo.html", context)
     



























