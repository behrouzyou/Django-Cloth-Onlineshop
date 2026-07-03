from django.urls import include, path
from rest_framework.routers import DefaultRouter

from products.view.api.product_view_set import ProductViewSet
from products.view.product_list_view import ProductListView
from products.view.product_view import ProductView

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('api/products/', include(router.urls)),
    path('product/<int:pk>/', ProductView.as_view()),
    path('products/', ProductListView.as_view()),
]
