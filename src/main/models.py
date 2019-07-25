from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

def image_directory_path(instance, filename):
    return 'property_{0}/{1}'.format(instance.property.id, filename)

# Create your models here.
class Dashboard(models.Model):
    """
    Each user that signs up will be assigned their on Dashboard
    containing their property they have announced for rent
    """
    dashboard_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Location(models.Model):
    num = models.IntegerField(null=True, blank=True, default=None)
    address = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)

class Property(models.Model):
    """
    Links Location of the property and dashboard
    """
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    num_guests = models.IntegerField(null=True, blank=True)
    num_rooms = models.IntegerField(null=True, blank=True)
    time_booked = models.IntegerField(default=0)
    description = models.CharField(null=True, blank=True, max_length=10000000000)
    display_image = models.ImageField(null=True, blank=True, upload_to=image_directory_path)
    # facilities
    free_parking = models.BooleanField(null=True, blank=True, default=False)
    pool = models.BooleanField(null=True, blank=True, default=False)
    gym = models.BooleanField(null=True, blank=True, default=False)
    spa = models.BooleanField(null=True, blank=True, default=False)
    # disability access
    ramp = models.BooleanField(null=True, blank=True, default=False)
    travelator = models.BooleanField(null=True, blank=True, default=False)
    elevator = models.BooleanField(null=True, blank=True, default=False)
    # property Type
    apartment = models.BooleanField(null=True, blank=True, default=False)
    hotel = models.BooleanField(null=True, blank=True, default=False)
    house = models.BooleanField(null=True, blank=True, default=False)
    resort = models.BooleanField(null=True, blank=True, default=False)
    townhouse = models.BooleanField(null=True, blank=True, default=False)
    # amenities
    kitchen = models.BooleanField(null=True, blank=True, default=False)
    airconditioning = models.BooleanField(null=True, blank=True, default=False)
    bathroom = models.BooleanField(null=True, blank=True, default=False)
    tv = models.BooleanField(null=True, blank=True, default=False)
    

    def is_matching_num_rooms(self, _num_rooms):
        if (self.num_rooms == _num_rooms):
            return True
        return False

    def is_more_than_guests(self, _num_guests):
        if (self.num_guests < _num_guests):
            return False
        return True

    def time_booked_incr(self):
        self.time_booked += 1
        self.save()

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)

    def date_overlapping(self, check_in, check_out):
        return (self.start_date <= check_out and self.end_date >= check_in)


class image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path)
