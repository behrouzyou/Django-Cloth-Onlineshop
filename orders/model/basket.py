from django.contrib.auth.models import User
from django.db import models

from products.model.product import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    guest_id = models.CharField(max_length=255, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"{self.product.name} in basket of {self.user.username}"
        return f"{self.product.name} in basket of guest {self.guest_id}"

    def get_total_price(self):
        return self.quantity * self.product.price
