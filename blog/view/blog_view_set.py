from rest_framework.viewsets import ReadOnlyModelViewSet

from blog.model.blog import Blog
from blog.model.serializer.blog_serializer import BlogSerializer


class BlogViewSet(ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
