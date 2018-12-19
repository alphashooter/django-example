from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request, 'index.html', {'products': data})
