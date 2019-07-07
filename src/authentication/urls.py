from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name="logout"),
]
