from django.urls import path

from orders.view.add_to_basket_view import AddToBasketView
from orders.view.basket_view import BasketView
from orders.view.payment_view import PaymentView
from orders.view.register_view import RegisterView

urlpatterns = [
    path('basket/<int:product_id>/add/', AddToBasketView.as_view()),
    path('basket/', BasketView.as_view()),
    path('register/', RegisterView.as_view()),
    path('pay/', PaymentView.as_view()),
]
