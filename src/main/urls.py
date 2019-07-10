from django.urls import path
from . import views, dashboard     # from current path import views.py

urlpatterns=[
    path("", views.index, name="index"),        
    path("about", views.about, name="about"),
    path("howto", views.howto, name="howto"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create_property", dashboard.create_property, name="create property"),
    path("dashboard/delete-property/<int:id>", dashboard.delete_property, name="delete property"),
]
