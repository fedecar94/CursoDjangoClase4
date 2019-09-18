from crispy_forms.layout import Div, Field, Layout
from django import forms
from django.contrib.auth import get_user_model
from django.utils import timezone
from markdownx.fields import MarkdownxFormField

from crispy_forms.helper import FormHelper

from blog.models import Publicacion


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
        contenido.css_class = 'col-12'
        row = Div(titulo, fecha_publicacion, contenido)
        row.css_class = 'row'
        self.helper.layout = Layout(row)
        super(PublicacionForm, self).__init__(*args, **kwargs)
