from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

def image_directory_path(instance, filename):
    return 'property_{0}/{1}'.format(instance.property.id, filename)

def image_directory_path_display(instance, filename):
    return 'display_property_{0}/{1}'.format(instance.id, filename)

# Create your models here.
class Dashboard(models.Model):
    dashboard_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Location(models.Model):
    num = models.IntegerField(null=True, blank=True, default=None)
    street = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    post_code = models.IntegerField()
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)

class Property(models.Model):
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    num_guests = models.IntegerField(null=True, blank=True)
    num_rooms = models.IntegerField(null=True, blank=True)
    time_booked = models.IntegerField(default=0)
    description = models.CharField(null=True, blank=True, max_length=10000000000)
    # property Type
    property_type = models.CharField(null=True, blank=True, max_length=30)
    # facilities
    free_parking = models.BooleanField(null=True, blank=True, default=False)
    pool = models.BooleanField(null=True, blank=True, default=False)
    gym = models.BooleanField(null=True, blank=True, default=False)
    spa = models.BooleanField(null=True, blank=True, default=False)
    # disability access
    ramp = models.BooleanField(null=True, blank=True, default=False)
    travelator = models.BooleanField(null=True, blank=True, default=False)
    elevator = models.BooleanField(null=True, blank=True, default=False)
    # amenities
    kitchen = models.BooleanField(null=True, blank=True, default=False)
    airconditioning = models.BooleanField(null=True, blank=True, default=False)
    bathroom = models.BooleanField(null=True, blank=True, default=False)
    tv = models.BooleanField(null=True, blank=True, default=False)
    wifi = models.BooleanField(null=True, blank=True, default=False)
    laundry = models.BooleanField(null=True, blank=True, default=False)
    

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

    def num_of_reviews(self):
        reviews = Property_review.objects.filter(property__id=self.id)
        return len(reviews)

    def execellent_rating(self):
        reviews = Property_review.objects.filter(property__id=self.id, rating=5)
        return len(reviews)

    def range_avg_rating(self):
        reviews = Property_review.objects.filter(property__id=self.id)
        avg = 0
        for r in reviews:
            avg += r.rating
        if (len(reviews) == 0):
            avg = 5
        else:
            avg = avg / len(reviews)
        return range(int(avg))

    def avg_rating(self):
        reviews = Property_review.objects.filter(property__id=self.id)
        avg = 0
        for r in reviews:
            avg += r.rating
        if (len(reviews) == 0):
            avg = 5
        else:
            avg = avg / len(reviews)
        return int(avg)


    def avg_cleanliness(self):
        reviews = Property_review.objects.filter(property__id=self.id)
        avg = 0
        for r in reviews:
            avg += r.cleanliness
        if (len(reviews) == 0):
            avg = 5
        else:
            avg = avg / len(reviews)
        return float(avg/5) * 100
            
    def avg_communication(self):
        reviews = Property_review.objects.filter(property__id=self.id)
        avg = 0
        for r in reviews:
            avg += r.communication
        if (len(reviews) == 0):
            avg = 5
        else:
            avg = avg / len(reviews)
        return float(avg/5) * 100

    def avg_value(self):
        reviews = Property_review.objects.filter(property__id=self.id)
        avg = 0
        for r in reviews:
            avg += r.value
        if (len(reviews) == 0):
            avg = 5
        else:
            avg = avg / len(reviews)
        return float(avg/5) * 100

    def avg_location(self):
        reviews = Property_review.objects.filter(property__id=self.id)
        avg = 0
        for r in reviews:
            avg += r.location
        if (len(reviews) == 0):
            avg = 5
        else:
            avg = avg / len(reviews)
        return float(avg/5) * 100

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    reviewed = models.BooleanField(default=False)

    def date_overlapping(self, check_in, check_out):
        return (self.start_date <= check_out and self.end_date >= check_in)


class image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path)


class Property_review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    review = models.CharField(max_length=10000000000)
    rating = models.IntegerField(default=0)
    cleanliness = models.IntegerField(default=0)
    communication = models.IntegerField(default=0)
    value = models.IntegerField(default=0)
    location = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)

    def range_rating(self):
        return range(self.rating)

class Activities(models.Model):
    url = models.CharField(max_length=100000)
    image_url = models.CharField(max_length=100000)
    title = models.CharField(max_length=20)
