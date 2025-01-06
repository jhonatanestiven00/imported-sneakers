from django.db import models

#tipos de campo
# https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types

class ServiceDB(models.Model):
    title= models.CharField(verbose_name='titulo',max_length=200)
    subtitle= models.CharField(verbose_name='subtitulo',max_length=200)
    content= models.TextField(verbose_name='contenido')
    image= models.ImageField(verbose_name='imagen')
    created=models.DateTimeField(verbose_name="fecha de creacion", auto_now_add=True)
    updated= models.DateTimeField(verbose_name="fecha de actualizacion", auto_now=True)

    class Meta:
        verbose_name= "servicio"
        verbose_name_plural= "servicios"
        ordering=["created"]
    
    def __str__(self):
        return self.title
