from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from core.model.navigation import Navigation
from orders.model.address import Address
from orders.model.basket import Basket
from orders.util.basket_util import get_guest_id


class RegisterView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect('/pay/')
        navigations = Navigation.objects.filter(is_active=True)
        context = {
            'navigations': navigations
        }
        return render(request, 'register.html', context)

    def post(self, request: HttpRequest):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')

        if User.objects.filter(username=mobile).exists():
            messages.success(request,
                             'شما قبلا با این شماره موبایل ثبت نام کرده اید. لطفا ابتدا وارد سایت شوید.',
                             extra_tags='danger')
            return redirect('/register/')

        user = User.objects.create_user(
            username=mobile,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_staff = True
        user.save()

        customer_group = Group.objects.get(name='Customer')
        user.groups.add(customer_group)

        Address.objects.create(
            user=user,
            mobile=mobile,
            addr=address,
            postal_code=postal_code
        )

        guest_id = get_guest_id(request)
        Basket.objects.filter(guest_id=guest_id).update(user=user)

        login(request, user)

        return redirect('/pay/')
