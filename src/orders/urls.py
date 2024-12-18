from django.urls import path
from .views import order_create, order_list, order_success


urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('list/', order_list, name='order_list'),
    path('success/', order_success, name='order_success'),
]