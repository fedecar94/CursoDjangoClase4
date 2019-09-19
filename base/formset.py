"""Clases donde se guardan los layout de los formsets"""
from crispy_forms.layout import LayoutObject, TEMPLATE_PACK
from django.template.loader import render_to_string


class Formset(LayoutObject):
    """Generic layout for a formset"""
    template = "extras/formset.html"

    def __init__(self, formset_name_in_context, template=None):
        self.formset_name_in_context = formset_name_in_context
        self.fields = []
        if template:
            self.template = template

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        """Render del layout"""
        formset = context[self.formset_name_in_context]
        return render_to_string(self.template, {'formset': formset})
