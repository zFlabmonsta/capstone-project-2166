from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login

from main.models import Dashboard, Property, Location, Booking, Property_review
from .forms import Review_form

from datetime import datetime, date, time

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
