from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=200,verbose_name='Titulo')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripcion')
    imagen = models.ImageField(upload_to='imagenes_cursos/', blank=True, null=True, verbose_name='Imagen')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    
    #clase agregada para modelo curso
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['fecha_creacion']

    def __str__(self):
        return self.titulo