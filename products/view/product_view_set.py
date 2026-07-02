from rest_framework.viewsets import ReadOnlyModelViewSet

from products.model.product import Product
from products.model.serializer.product_serializer import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
