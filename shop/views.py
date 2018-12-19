from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import *


def index(request):
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            'title': product.title,
            'price': product.price,
            'currency': product.currency.code
        })

    user: User = request.user
    if user.is_authenticated:
        username = user.username
    else:
        username = None

    context = {
        'products': data,
        'username': username
    }

    return render(request, 'index.html', context)


def log_out(request):
    logout(request)
    return redirect('index')


def log_in(request):
    user: User = request.user
    if user.is_authenticated:
        return redirect('index')

    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return render(request, 'login.html')

    login(request, user)
    return redirect('index')
