from django.views.generic import ListView
from blog.model.blog import Blog
from core.model.navigation import Navigation


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'
    navigtaions=Navigation.objects.filter(is_active=True)
    paginate_by = 3
    extra_context = {
        'navigations':navigtaions
    }