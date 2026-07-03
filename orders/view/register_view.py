from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from core.model.navigation import Navigation


class RegisterView(View):
    def get(self,request:HttpRequest):
        if request.user.is_authenticated:
            return redirect("/pay/")
        navigations = Navigation.objects.filter(is_active=True)
        context={
            'navigations':navigations
        }
        return render(request,'register.html',context=context)
    def post(self,request:HttpRequest):
        pass