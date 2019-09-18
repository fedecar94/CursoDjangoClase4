from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from blog.forms import PublicacionForm
from blog.models import Publicacion


class PublicacionListView(LoginRequiredMixin, ListView):
    template_name = 'blog/publicacion/list.html'
    model = Publicacion

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(autor=self.request.user)
        return query


class PublicacionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/publicacion/create.html'
    model = Publicacion
    form_class = PublicacionForm
    success_url = reverse_lazy('publicacion_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/publicacion/create.html'
    model = Publicacion
    form_class = PublicacionForm
    success_url = reverse_lazy('publicacion_list')

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(autor=self.request.user)
        return query

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'blog/publicacion/delete.html'
    model = Publicacion
    success_url = reverse_lazy('publicacion_list')

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(autor=self.request.user)
        return query
