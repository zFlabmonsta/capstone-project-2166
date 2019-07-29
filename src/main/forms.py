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
    #disability access
    ramp = forms.BooleanField(required=False, initial=False)
    travelator = forms.BooleanField(required=False, initial=False)
    elevator = forms.BooleanField(required=False, initial=False)
    #Property Type
    apartment = forms.BooleanField(required=False, initial=False)
    hotel = forms.BooleanField(required=False, initial=False)
    house = forms.BooleanField(required=False, initial=False)
    resort = forms.BooleanField(required=False, initial=False)
    townhouse = forms.BooleanField(required=False, initial=False)
    #amenities    
    kitchen = forms.BooleanField(required=False, initial=False)
    tv = forms.BooleanField(required=False, initial=False)
    bathroom = forms.BooleanField(required=False, initial=False)
    airconditioning = forms.BooleanField(required=False, initial=False)

class Search_property_form (forms.Form):
    where = forms.CharField(label='Where', max_length=100)
    check_in = forms.DateTimeField(label='Check in', initial=datetime.now().date)
    check_out = forms.DateTimeField(label='Check out', initial=datetime.now().date)
    num_guests = forms.IntegerField(label='Guests')
    num_rooms = forms.IntegerField(label='Rooms')

RATING = [
    (1, 'Poor'),
    (2, 'Mediocre'),
    (3, 'Okay'),
    (4, 'Good'),
    (5, 'Execellent')
]
class Review_form(forms.Form):
    review = forms.CharField(label='Review', widget=forms.Textarea, max_length=1000000000)
    rating = forms.CharField(label='Rate your experience' , widget=forms.Select(choices=RATING))

class Filter_facilities(forms.Form):
    free_parking = forms.BooleanField(label="Free Parking", required=False, initial=False, widget=forms.CheckboxInput())
    pool = forms.BooleanField(label="Pool", required=False, initial=False, widget=forms.CheckboxInput())
    gym = forms.BooleanField(label="Gym", required=False, initial=False, widget=forms.CheckboxInput())
    spa = forms.BooleanField(label="Spa", required=False, initial=False, widget=forms.CheckboxInput())

class Filter_disability_access(forms.Form):
    ramp = forms.BooleanField(label="Ramp", required=False, initial=False, widget=forms.CheckboxInput())
    travelator = forms.BooleanField(label="Travelator", required=False, initial=False, widget=forms.CheckboxInput())
    elevator = forms.BooleanField(label="Elevator", required=False, initial=False, widget=forms.CheckboxInput())

class Filter_property_type(forms.Form):
    apartment = forms.BooleanField(label="Apartment", required=False, initial=False, widget=forms.CheckboxInput())
    hotel = forms.BooleanField(label="Hotel", required=False, initial=False, widget=forms.CheckboxInput())
    house = forms.BooleanField(label="House", required=False, initial=False, widget=forms.CheckboxInput())
    resort = forms.BooleanField(label="Resort", required=False, initial=False, widget=forms.CheckboxInput())
    townhouse = forms.BooleanField(label="Townhouse", required=False, initial=False, widget=forms.CheckboxInput())

class Filter_amenities(forms.Form):
    tv = forms.BooleanField(label="TV", required=False, initial=False, widget=forms.CheckboxInput())
    bathroom = forms.BooleanField(label="Bathroom", required=False, initial=False, widget=forms.CheckboxInput())
    kitchen = forms.BooleanField(label="Kitchen", required=False, initial=False, widget=forms.CheckboxInput())
    airconditioning = forms.BooleanField(label="Air Conditioning", required=False, initial=False, widget=forms.CheckboxInput())

