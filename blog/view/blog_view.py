from django.views.generic import TemplateView
from rest_framework.generics import get_object_or_404

from blog.model.blog import Blog
from core.model.navigation import Navigation


class BlogView(TemplateView):
    template_name = 'blog.html'

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        blog = get_object_or_404(Blog, pk=pk)
        blog.visit_count += 1
        blog.save(update_fields=['visit_count'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        blog = Blog.objects.get(pk=pk)
        navigations = Navigation.objects.filter(is_active=True)
        context['blog'] = blog
        context['navigations'] = navigations
        return context
