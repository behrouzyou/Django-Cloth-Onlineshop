from django.views.generic import TemplateView
from rest_framework.generics import get_object_or_404

from core.model.navigation import Navigation
from products.model.product import Product


class ProductView(TemplateView):
    template_name = 'product.html'

    # 1 dispatch
    # 2 get/post/put/delete
    # 3 get_context_data

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        product.visit_count += 1
        product.save(update_fields=['visit_count'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        navigations = Navigation.objects.filter(is_active=True)
        context['product'] = product
        context['navigations'] = navigations
        return context
