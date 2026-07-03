from django.db import models

from orders.model.enumeration.payment_status import PaymentStatus
from orders.model.order import Order


class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=0,verbose_name='مبلغ')
    status = models.CharField(max_length=10, choices=PaymentStatus.choices, default=PaymentStatus.PENDING,
                              verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد')
    payment_gateway = models.CharField(max_length=50, default='ZarinPal',verbose_name='درگاه پرداخت')

    def __str__(self):
        return f"x{self.pk} {self.status}"
    class Meta:
        verbose_name='تراکنش'
        verbose_name_plural='تراکنش ها'