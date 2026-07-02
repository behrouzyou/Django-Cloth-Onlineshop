from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.view.blog_view_set import BlogViewSet
from products.view.product_view_set import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
