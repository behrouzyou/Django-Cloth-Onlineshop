from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.views import View
from rest_framework.generics import get_object_or_404

from orders.model.basket import Basket
from orders.util.basket_util import get_guest_id
from products.model.product import Product


class AddToBasketView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        basket_item = self.get_or_create_basket_item(request, product)
        basket_item.quantity += 1
        basket_item.save()

        return JsonResponse({'message': 'به سبد خرید شما اضافه شد'})

    def get_or_create_basket_item(self, request: HttpRequest, product):
        if request.user.is_authenticated:
            return Basket.objects.get_or_create(user=request.user, product=product)[0]

        guest_id = get_guest_id(request)
        return Basket.objects.get_or_create(guest_id=guest_id, product=product)[0]
