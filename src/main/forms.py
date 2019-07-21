from django import forms
from datetime import datetime, date, time

class Property_form (forms.Form):
    num = forms.IntegerField(label="Number/Unit")
    street = forms.CharField(label='Street', max_length=50)
    post_code = forms.IntegerField(label='Post Code', max_value=9999)
    suburb = forms.CharField(label='Suburb', max_length=50)
    price = forms.IntegerField(label='Price')
    num_guests = forms.IntegerField(label='Guests')
    num_rooms = forms.IntegerField(label='Rooms')
    # images = 

class Search_property_form (forms.Form):
    where = forms.CharField(label='Where', max_length=100)
    check_in = forms.DateTimeField(label='Check in', initial=datetime.now().date)
    check_out = forms.DateTimeField(label='Check out', initial=datetime.now().date)
    num_guests = forms.IntegerField(label='Guests')
    num_rooms = forms.IntegerField(label='Rooms')
