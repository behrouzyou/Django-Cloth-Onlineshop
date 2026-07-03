from django.db import models


class PaymentStatus(models.TextChoices):
    PENDING = 'PENDING', 'در انتظار پرداخت'
    PAID = 'PAID', 'پرداخت شده'
    CANCELED = 'CANCELED', 'لغو شده'
    FAILED = 'FAILED', 'ناموفق'
