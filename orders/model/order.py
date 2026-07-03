from django.contrib.auth.models import User
from django.db import models

from orders.model.enumeration.payment_status import PaymentStatus


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='کاربر')
    status = models.CharField(max_length=10, choices=PaymentStatus.choices, default=PaymentStatus.PENDING,
                              verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='ویرایش')
    amount = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"سفارش #{self.pk} - {self.status}"

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
