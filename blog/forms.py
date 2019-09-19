from crispy_forms.layout import Div, Field, Layout
from django import forms
from django.contrib.auth import get_user_model
from django.forms import inlineformset_factory
from markdownx.fields import MarkdownxFormField

from crispy_forms.helper import FormHelper

from base.formset import Formset
from blog.models import Publicacion, Tag


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        exclude = ()

    def clean_etiqueta(self):
        etiqueta = self.cleaned_data.get('etiqueta')
        return etiqueta.replace(' ', '_')


TagFormSet = inlineformset_factory(
    Publicacion, Tag, form=TagForm,
    fields=['etiqueta'], extra=1, min_num=0, can_delete=True
    )


class PublicacionForm(forms.ModelForm):
    contenido = MarkdownxFormField()
    autor = forms.ModelChoiceField(get_user_model().objects.all(), required=False)

    class Meta:
        model = Publicacion
        fields = ['autor', 'titulo', 'fecha_publicacion', 'contenido']
        widgets = {
            'fecha_publicacion': forms.SelectDateWidget(attrs={'style': 'width: 32%; display: inline-block'})
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        fecha_publicacion = Div(Field('fecha_publicacion'))
        fecha_publicacion.css_class = 'col-md-4'
        titulo = Div(Field('titulo'))
        titulo.css_class = 'col-md-8'
        contenido = Div(Field('contenido'))
        contenido.css_class = 'col-8'
        tags = Div(Formset('tags'))
        tags.css_class = 'col-4'
        row = Div(titulo, fecha_publicacion, contenido, tags)
        row.css_class = 'row'
        self.helper.layout = Layout(row)
        super(PublicacionForm, self).__init__(*args, **kwargs)
