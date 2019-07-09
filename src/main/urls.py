from django.urls import path
from . import views     # from current path import views.py

urlpatterns=[
    path("", views.index, name="index"),        
    path("about", views.about, name="about"),
    path("howto", views.howto, name="howto"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create_property", views.create_property, name="create property"),
    path("dashboard/delete-property/<int:id>", views.delete_property, name="delete property"),
]
