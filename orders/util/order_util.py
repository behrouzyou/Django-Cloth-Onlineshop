from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, get_object_or_404

from orders.model.order import Order


def get_last_order(request: HttpRequest):
    order_pk = request.session['last_order_pk']
    if not order_pk:
        messages.error(request, 'سفارشی برای پرداخت یافت نشد', extra_tags='danger')
        return redirect('/')

    order = get_object_or_404(Order, pk=order_pk)
    return order
