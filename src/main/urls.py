from django.urls import path
from . import views, dashboard, booking     # from current path import views.py

urlpatterns=[
    path("", views.index, name="index"),        
    path("about", views.about, name="about"),
    path("moreinfo/map/<str:lat>/<str:lng>", views.map, name="map"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("moreinfo/<int:property_id>/<int:i_year>/<int:i_month>/<int:i_day>/<int:o_year>/<int:o_month>/<int:o_day>", 
        views.moreinfo, name="more info"),
]

urlpatterns += [
    path("create_property", dashboard.create_property, name="create property"),
    path("dashboard/delete-property/<int:id>", dashboard.delete_property, name="delete property"),
    path("make-booking/<int:property_id>/<int:i_year>/<int:i_month>/<int:i_day>/<int:o_year>/<int:o_month>/<int:o_day>", 
        booking.make_booking, name="make booking"),
    path("dashboard/delete-booking/<int:id>", dashboard.delete_booking, name="delete property"),
]

