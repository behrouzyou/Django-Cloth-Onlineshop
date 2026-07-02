from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.view.blog_view_set import BlogViewSet

router = DefaultRouter()
router.register('', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
