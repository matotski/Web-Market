from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to="static/vendor/media/users", default="static/vendor/media/users/default.svg", blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
