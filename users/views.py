from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegisterForm


# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('store:products'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            print('ok')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
