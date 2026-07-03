from django.contrib import admin

from orders.model.order_item import OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    fields = ('product', 'quantity', 'price')
