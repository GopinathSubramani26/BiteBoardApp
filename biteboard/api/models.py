from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = None  # Remove the inherited username field
    pin = models.CharField(max_length=6, blank=True, null=True)

    objects = UserManager()  # Use the custom manager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

