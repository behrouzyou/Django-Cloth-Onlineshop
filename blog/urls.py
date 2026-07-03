from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.view.api.blog_view_set import BlogViewSet
from blog.view.blog_list_view import BlogListView
from blog.view.blog_view import BlogView

router = DefaultRouter()
router.register('', BlogViewSet)

urlpatterns = [
    path('api/blog/', include(router.urls)),
    path('blog/', BlogListView.as_view()),
    path('blog/<int:pk>/', BlogView.as_view()),
]
