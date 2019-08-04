from django.urls import path
from . import views, dashboard, booking, property_list     # from current path import views.py

urlpatterns=[
    path("", views.index, name="index"),        
    path("about", views.about, name="about"),
    path("myaccount",views.myAccount, name="my account"),
]

# dashboard
urlpatterns += [
    path("dashboard", dashboard.dashboard, name="dashboard"),
    path("dashboard/delete-property/<int:id>", property_list.delete_property, name="delete property"),
    path("dashboard/delete-booking/<int:id>", booking.delete_booking, name="delete booking"),
    path("dashboard/edit-property-listing/<int:id>", property_list.edit_property_listing, name="edit property listing"),
    path("dashboard/give-review/<int:id>", booking.give_review, name="give review"),
]

# creation
urlpatterns += [
    path("create_property", property_list.create_property, name="create property"),
    path("make-booking/<int:property_id>/<int:i_year>/<int:i_month>/<int:i_day>/<int:o_year>/<int:o_month>/<int:o_day>", 
        booking.make_booking, name="make booking"),
]

# moreinfo
urlpatterns += [
    path("moreinfo/map/<str:lat>/<str:lng>", views.map, name="map"),
    path("moreinfo/<str:which>/<int:property_id>/<int:i_year>/<int:i_month>/<int:i_day>/<int:o_year>/<int:o_month>/<int:o_day>", 
        views.moreinfo, name="more info"),
    path("moreinfo/<str:which>/<int:id>", dashboard.moreinfo, name="more info-dashboard"),
]
