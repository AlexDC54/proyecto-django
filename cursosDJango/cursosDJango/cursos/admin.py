from django.contrib import admin
from .models import Curso
from django.utils.html import format_html

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion','imagen_preview')
    ordering = ('fecha_creacion',)
    search_fields = ('titulo','descripcion')
    list_filter = ('fecha_creacion', 'titulo')  #filtro para fecha y título
    date_hierarchy = 'fecha_creacion'

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.imagen.url))
        return ''
    imagen_preview.short_description = 'Vista Previa de Imagen'

