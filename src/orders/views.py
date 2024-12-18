from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Basket


@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            baskets = Basket.objects.filter(user=request.user)
            for basket in baskets:
                OrderItem.objects.create(
                    order=order,
                    product=basket.product,
                    quantity=basket.quantity,
                    price=basket.product.price
                )

            baskets.delete()

            return HttpResponseRedirect(reverse('order_success'))
        else:
            print(form.errors)

    else:
        form = OrderForm()

    context = {
        'form': form,
    }
    return render(request, 'orders/order_create.html', context)


@login_required
def order_list(request):
    user_orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'orders': user_orders,
    }
    return render(request, 'orders/order_list.html', context)


def order_success(request):
    return render(request, 'orders/order_success.html')
