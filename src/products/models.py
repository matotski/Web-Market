from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def str(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images', default='products_images/product.png')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    def str(self):
        return f'{self.name} ({self.category}) - {self.price}'