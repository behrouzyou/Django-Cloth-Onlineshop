from statistics import quantiles

from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View

from orders.model.basket import Basket
from orders.model.order import Order
from orders.model.order_item import OrderItem
from orders.model.transaction import Transaction


class PaymentView(View):
    def get(self, request: HttpRequest):
        if not request.user.is_authenticated:
            messages.error(request, 'لطفا ابتدا وارد حساب کاربری خود شوید', extra_tags='danger')
            return redirect('/')
        basket_items = Basket.objects.filter(user=request.user)

        if not basket_items.exists():
            messages.error(request, 'سبد خرید شما خالی است', extra_tags='danger')
            return redirect('/products/')

        total_price = 0
        for item in basket_items:
            total_price += item.get_total_price()

        order = Order.objects.create(
            user=request.user,
            amount=total_price
        )

        for item in basket_items:
            order_item = OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        transaction = Transaction.objects.create(
            order=order,
            amount=total_price,
            payment_gateway='LocalPayment'
        )

        # todo: go to Internet Payment Gateway (درگاه پرداخت اینترنتی)
        ipg = 'http://127.0.0.1:8000/ipg/'
        return redirect(ipg)
