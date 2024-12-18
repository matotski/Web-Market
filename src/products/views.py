from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Product, Basket
from django.urls import reverse


def main(request):
    return render(request, 'products/main.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', context={'products': products})

def product_detail(request, product_id: id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product_detail.html', context={'product': product})


@login_required
def basket_add(request, product_id: id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)

    basket = baskets.first()
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


