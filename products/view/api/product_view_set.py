from rest_framework.viewsets import ReadOnlyModelViewSet

from products.model.product import Product
from products.model.serializer.product_serializer import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
