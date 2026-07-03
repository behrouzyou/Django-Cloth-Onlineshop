from django.db import models

from orders.model.order import Order
from products.model.product import Product


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='سفارش')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='محصول')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='تعداد')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} #{self.order.pk}"

    class Meta:
        verbose_name = 'قلم'
        verbose_name_plural = 'اقلام'
