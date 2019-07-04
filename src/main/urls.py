from django.urls import path
from . import views     # from current path import views.py

urlpatterns=[
    path("", views.index, name="index"),        
]
