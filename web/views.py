from django.utils import timezone
from django.views.generic import ListView, DetailView

from blog.models import Publicacion


class Home(ListView):
    model = Publicacion
    template_name = 'web/home.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(fecha_publicacion__lte=timezone.now())
        return query


class Detalle(DetailView):
    model = Publicacion
    template_name = 'web/detalle.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(fecha_publicacion__lte=timezone.now())
        return query
