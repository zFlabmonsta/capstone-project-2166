from django.contrib import admin

from .models import Property, Location, image

admin.site.register(Property)
admin.site.register(Location)
admin.site.register(image)

# Register your models here.
