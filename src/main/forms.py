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
    description = forms.CharField(label='description', widget=forms.Textarea, max_length=1000000000)
    image = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    #facilities
    free_parking = forms.BooleanField(required=False, initial=False)
    pool = forms.BooleanField(required=False, initial=False)
    gym = forms.BooleanField(required=False, initial=False)
    spa = forms.BooleanField(required=False, initial=False)

class Search_property_form (forms.Form):
    where = forms.CharField(label='Where', max_length=100)
    check_in = forms.DateTimeField(label='Check in', initial=datetime.now().date)
    check_out = forms.DateTimeField(label='Check out', initial=datetime.now().date)
    num_guests = forms.IntegerField(label='Guests')
    num_rooms = forms.IntegerField(label='Rooms')

class Filter_facilities(forms.Form):
    free_parking = forms.BooleanField(label="Free Parking", required=False, initial=False, widget=forms.CheckboxInput())
    pool = forms.BooleanField(label="Pool", required=False, initial=False, widget=forms.CheckboxInput())
    gym = forms.BooleanField(label="Gym", required=False, initial=False, widget=forms.CheckboxInput())
    spa = forms.BooleanField(label="Spa", required=False, initial=False, widget=forms.CheckboxInput())
