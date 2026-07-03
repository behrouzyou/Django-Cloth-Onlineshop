from django.views.generic import TemplateView

from core.model.navigation import Navigation


class AboutView(TemplateView):
    template_name = 'about.html'
    navigations = Navigation.objects.filter(is_active=True)
    extra_context = {
        'navigations': navigations
    }
