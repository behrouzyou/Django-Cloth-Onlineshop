from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from core.model.navigation import Navigation
from orders.model.basket import Basket
from orders.model.enumeration.payment_status import PaymentStatus
from orders.util.order_util import get_last_order


class VerifyView(View):
    def get(self,request:HttpRequest):
        status=request.GET.get('status')
        order=get_last_order(request)
        transactions=order.transactions.last()

        if status=='OK':
            order.status=PaymentStatus.PAID
            transactions.status=PaymentStatus.PAID
            Basket.objects.filter(user=request.user).delete()
            messages.success(request,'پرداخت شما با موفقیت انجام شد')
        elif status == 'NOK':
            order.status=PaymentStatus.FAILED
            transactions.status=PaymentStatus.FAILED
            messages.error(request,'پرداخت ناموفق بود',extra_tags='danger')
        order.save()
        transactions.save()
        navigations=Navigation.objects.filter(is_active=True)
        context={
            'navigations':navigations,
            'order':order,
            'transactions':transactions
        }
        return render(request,'verify.html',context=context)