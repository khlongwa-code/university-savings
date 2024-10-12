from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import LoginForm, RegistrationForm
from .models import Income

# Create your views here.

def home_view(request):
    user = request.user
    login_form = LoginForm()
    signup_form = RegistrationForm()

    context = {
            'login_form': login_form,
            'signup_form': signup_form,
            'is_authenticated': request.user.is_authenticated,
        }

    if user.is_authenticated:
        context['registered_user'] = user.first_name

    return render(request, 'base.html', context)

def signin_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return redirect('home')

def signout_view(request):
    logout(request)
    return redirect('home')