from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dashboard(models.Model):
    """
    Each user that signs up will be assigned their on Dashboard
    containing their property they have announced for rent
    """
    dashboard_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Location(models.Model):
    street = models.CharField(max_length=100)
    post_code = models.CharField(max_length=4)
    suburb = models.CharField(max_length=100)

class Property(models.Model):
    """
    Links Location of the property and dashboard
    """
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # image
