
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create the user with hashed password
            user = form.save(commit=False)  # Don't save to the database yet
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Now save the user to the database

            # Log the user in immediately after successful registration
            login(request, user)

            # Redirect to a success page or wherever you want the user to go after registering
            return redirect('home')  # Redirect to home or any other page
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('top')

@login_required
def home_view(request):
    return render(request, 'home.html')