from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

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
    # image

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)

    def date_overlapping(self, check_in, check_out):
        return (self.start_date < check_out or self.end_date > check_in)
