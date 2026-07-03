from django.contrib import admin

from core.model.navigation import Navigation
from orders.model.order import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'amount', 'created_at')
    list_filter = ('status',)
    search_fields = ('user', 'status',)
