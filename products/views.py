from django.shortcuts import render

from products.models import Product
# Create your views here.


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')
