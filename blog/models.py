from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField


class Publicacion(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='publicaciones')
    titulo = models.CharField('Título', max_length=128)
    slug = models.SlugField('Slug', blank=True)
    fecha_publicacion = models.DateField('Fecha de publicación')
    contenido = MarkdownxField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.titulo)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return '{};{}'.format(self.id, self.slug)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-fecha_publicacion', ]
