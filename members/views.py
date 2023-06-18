from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserCreationForm

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Logged in successfully!"))
            return redirect("home")
        else:
            messages.error(request, ("Wrong credentials, try again!"))
            return redirect("login_user")

    return render(request, "members/login.html")

def register_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            messages.success(request, ("Registered successfully, you can log in now!"))
            return redirect("login_user")
        else:
            messages.error(request, ("Your form was not valid!"))
            return redirect("register_user")
    return render(request, "members/register.html", {"form":form})

@login_required(login_url="members/login/")
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("home")

