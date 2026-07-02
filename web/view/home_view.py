from django.views.generic import TemplateView

from core.model.navigation import Navigation
from core.model.slider import Slider
from products.model.product import Product


class HomeView(TemplateView):
    template_name = 'index.html'
    navigations = Navigation.objects.filter(is_active=True)
    sliders = Slider.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True).order_by('-created_at')[:6]
    extra_context = {
        'navigations': navigations,
        'sliders': sliders,
        'products': products
    }
