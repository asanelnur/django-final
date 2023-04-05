from django.shortcuts import render

from products.models import Product, ProductCategory


# Create your views here.

def index(request):
    context = {
        'title': 'Store',
        'username': 'Asan Elnur',
        'is_promotion': False
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'storeApp',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
