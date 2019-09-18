from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from blog.models import Publicacion

admin.site.register(Publicacion, MarkdownxModelAdmin)
