from django.contrib import admin

from core.model.navigation import Navigation
from orders.model.admin.order_item_admin import  OrderItemInline
from orders.model.admin.transaction_admin import TransactionInline
from orders.model.order import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'amount', 'created_at')
    list_filter = ('status',)
    search_fields = ('user', 'status',)
    inlines = [OrderItemInline,TransactionInline]
    def get_queryset(self, request):
        qs=super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
