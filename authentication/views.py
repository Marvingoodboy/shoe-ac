from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# User login view
def user_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, 'login.html')


# User logout View
def user_logout_view(request):
    auth.logout(request)
    return redirect('login')


# Redirect view from index to login page
def redirect_from_index_to_login(request):
    if User.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')


