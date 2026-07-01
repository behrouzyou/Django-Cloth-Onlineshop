from rest_framework import viewsets
from blog.model.blog import Blog
from blog.model.serializer.blog_serializer import BlogSerializer


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class =BlogSerializer