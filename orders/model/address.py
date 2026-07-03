from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    postal_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    addr = models.CharField(max_length=4000, default='')

    def __str__(self):
        return f"{self.user.username} {self.postal_code}"
