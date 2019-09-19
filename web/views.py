from django.db.models import Q
from django.utils import timezone
from django.views.generic import ListView, DetailView

from blog.models import Publicacion


class Home(ListView):
    model = Publicacion
    template_name = 'web/home.html'
    paginate_by = 5

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(fecha_publicacion__lte=timezone.now())
        if 'parametros' in self.request.GET:
            parametros = self.request.GET.get('parametros', '')
            for parametro in parametros.split(' '):
                query = query.filter(
                    Q(titulo__icontains=parametro) |
                    Q(contenido__icontains=parametro) |
                    Q(autor__first_name__icontains=parametro) |
                    Q(autor__last_name__icontains=parametro) |
                    Q(tags__etiqueta__icontains=parametro)
                )
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'parametros' in self.request.GET:
            context['parametros'] = self.request.GET.get('parametros')
        return context


class Detalle(DetailView):
    model = Publicacion
    template_name = 'web/detalle.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(fecha_publicacion__lte=timezone.now())
        return query
