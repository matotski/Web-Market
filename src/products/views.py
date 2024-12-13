from django.shortcuts import render
from .models import Product


def main(request):
    return render(request, 'products/main.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', context={'products':products})
