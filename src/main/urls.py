from django.urls import path
from . import views     # from current path import views.py

urlpatterns=[
    path("", views.index, name="index"),        
    path("about", views.about, name="about"),
    path("howto", views.howto, name="howto"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create_class", views.create_class, name="create class"),
]
