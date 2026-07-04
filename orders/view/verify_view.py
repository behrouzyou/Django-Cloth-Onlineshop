from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views import View

from core.model.navigation import Navigation
from orders.model.basket import Basket
from orders.model.enumeration.payment_status import PaymentStatus
from orders.model.transaction import Transaction
from orders.util.ipg import zarinpal_pay
from orders.util.order_util import get_last_order


class VerifyView(View):
    def get(self, request: HttpRequest):
        authority = request.GET.get('Authority')
        status = request.GET.get('Status')
        transaction = Transaction.objects.filter(authority=authority).first()

        if transaction is None:
            messages.error(request, 'تراکنشی با این شناسه یافت نشد!', extra_tags='danger')
            return render(request, 'verify.html')

        if status == 'OK' and transaction.status != PaymentStatus.PAID:
            zarinpal_pay.verify_payment(request, transaction)

        if transaction.status == PaymentStatus.PAID:
            Basket.objects.filter(user=request.user).delete()
            messages.success(request, 'پرداخت شما با موفقیت انجام شد')
        else:
            messages.error(request, 'پرداخت ناموفق بود!', extra_tags='danger')

        navigations = Navigation.objects.filter(is_active=True)
        context = {
            'navigations': navigations,
            'order': transaction.order,
            'transaction': transaction
        }
        return render(request, 'verify.html', context)
