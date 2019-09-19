from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from blog.forms import PublicacionForm, TagFormSet
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

    def get_context_data(self, **kwargs):
        data = super(PublicacionCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['tags'] = TagFormSet(self.request.POST)
        else:
            data['tags'] = TagFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['tags']
        if formset.is_valid():
            with transaction.atomic():
                form.instance.autor = self.request.user
                self.object = form.save()
                formset.instance = self.object
                formset.save()
                return HttpResponseRedirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(form=form))


class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/publicacion/create.html'
    model = Publicacion
    form_class = PublicacionForm
    success_url = reverse_lazy('publicacion_list')

    def get_context_data(self, **kwargs):
        data = super(PublicacionUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['tags'] = TagFormSet(self.request.POST, instance=self.object)
        else:
            data['tags'] = TagFormSet(instance=self.object)
        return data

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(autor=self.request.user)
        return query

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['tags']
        if formset.is_valid():
            with transaction.atomic():
                form.instance.autor = self.request.user
                self.object = form.save()
                formset.instance = self.object
                formset.save()
                return HttpResponseRedirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(form=form))


class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'blog/publicacion/delete.html'
    model = Publicacion
    success_url = reverse_lazy('publicacion_list')

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(autor=self.request.user)
        return query
