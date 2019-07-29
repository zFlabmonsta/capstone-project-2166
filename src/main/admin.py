from django.contrib import admin

from .models import Property, Location, image, Property_review

admin.site.register(Property)
admin.site.register(Location)
admin.site.register(image)
admin.site.register(Property_review)

# Register your models here.
