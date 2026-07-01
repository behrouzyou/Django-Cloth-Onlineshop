from rest_framework import viewsets
from products.model.product import Product
from products.model.serializer.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer