from django.http import HttpRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache

from core.model.navigation import Navigation
from orders.model.basket import Basket


class BasketView(View):
    @method_decorator(never_cache)
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            basket_items = Basket.objects.filter(user=request.user)
        else:
            guest_id = request.session.session_key
            if guest_id in None:
                request.session.create()
                guest_id=request.session.session_key
            basket_items = Basket.objects.filter(guest_id=guest_id)

        total_price = 0
        for item in basket_items:
            total_price += item.get_total_price()

        navigations = Navigation.objects.filter(is_active=True)
        context = {
            'basket_items': basket_items,
            'navigations': navigations,
            'total_price': total_price
        }
        return render(request, 'basket.html', context=context)
