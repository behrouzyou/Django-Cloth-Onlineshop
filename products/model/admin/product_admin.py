from django.contrib import admin

from products.model.product import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','is_active','created_at','visit_count')
    list_filter = ('is_active','created_at','updated_at')
    search_fields = ('name','description')
    list_editable = ('price','stock','is_active')