from django.views.generic.base import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'base/home.html'
