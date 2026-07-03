from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View

from core.model.navigation import Navigation
from orders.model.order import Order
from orders.util.order_util import get_last_order


class IPGView(View):
    def get(self,request:HttpRequest):
        order=get_last_order(request)
        navigations=Navigation.objects.filter(is_active=True)
        context={
            'navigations':navigations,
            'order':order
        }
        return render(request,'ipg.html',context)
