from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .backends import CustomAuthBackend
from .forms import SignInForm, SignUpForm
from .models import CustomUser


def sign_up(request):
    form = SignUpForm()
    action = reverse('sign_up')
    is_authenticated = request.user.is_authenticated

    context = {
        'form': form,
        'action': action,
        'button_value': 'Sign up',
        'is_authenticated': is_authenticated,
    }

    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            password = data['password']
            repeated_password = data['repeat_password']

            if password == repeated_password:
                user = CustomUser.objects.create_user(email=email, password=password, username=username)
                login(request, user)
                return redirect('chat')

    return render(request, 'users/authorization.html', context)


def sign_in(request):
    form = SignInForm()
    action = reverse('sign_in')
    is_authenticated = request.user.is_authenticated
    a = ''

    context = {
        'form': form,
        'action': action,
        'button_value': 'Sign in',
        'is_authenticated': is_authenticated,
    }

    if request.POST:
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data.get('email')
            password = data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                redirect('chat')

    return render(request, 'users/authorization.html', context)


def sign_out(request):
    logout(request)
    return redirect('chat')