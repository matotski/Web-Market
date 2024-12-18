from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='static/vendor/media/products_images', default='static/vendor/media/products_images/product.png')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} ({self.category}) - {self.price}'

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'Корзина для: {self.user.username}'

    def sum(self):
        return self.product.price * self.quantity