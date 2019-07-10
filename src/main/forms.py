from django import forms
from datetime import datetime, date, time

class Property_form (forms.Form):
    street = forms.CharField(label='Street', max_length=50)
    post_code = forms.CharField(label='Post Code', max_length=20)
    suburb = forms.CharField(label='Suburb', max_length=50)
    # images = 

class Search_property_form (forms.Form):
    where = forms.CharField(label='Where', max_length=100)
    check_in = forms.DateField(label='Check in', initial=datetime.now())
    check_out = forms.DateField(label='Check out')
    num_guests = forms.IntegerField(label='Guests')
