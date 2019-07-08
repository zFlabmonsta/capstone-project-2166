from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from main.models import Dashboard

# Create your views here.

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # create dashboard
            dashboard = Dashboard(dashboard_name = user.username + "dashboard", user=user)
            dashboard.save()
            return HttpResponseRedirect("/")
    return render(request, 'authentication/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            dashboard_id = Dashboard.objects.get(user=user.id).id
            return HttpResponseRedirect("dashboard")
        else:
            return HttpResponseRedirect('/')
    else:
        return render(request, 'authentication/login.html')
