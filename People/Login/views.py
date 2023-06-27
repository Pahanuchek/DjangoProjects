from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import UserLoginForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'Login/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Login')