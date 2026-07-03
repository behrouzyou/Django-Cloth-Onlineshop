from django.views.generic import ListView

from core.model.navigation import Navigation
from products.model.product import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 3
    navigtaion=Navigation.objects.filter(is_active=True)
    extra_context = {
        'navigations':navigtaion
    }