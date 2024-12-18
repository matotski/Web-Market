from django.urls import path
from .views import products, product_detail, basket_add, basket_remove

urlpatterns = [
    path('', products, name='products'),
    path('<int:product_id>', product_detail, name='product_detail'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]