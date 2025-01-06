from django.db import models

# Create your models here.
class PageDB(models.Model):
    title= models.CharField(verbose_name="Titulo", max_length=200)
    contents= models.TextField(verbose_name="Contenido")
    order= models.SmallIntegerField(verbose_name="Orden", default=0)
    created= models.DateTimeField(verbose_name="Fecha creacion", auto_now_add=True)
    updated=models.DateTimeField(verbose_name="Fecha actualización", auto_now=True)

    class Meta:
        verbose_name="pagina"
        verbose_name_plural="Paginas"
        ordering=['order','title']

    def __str__(self):
        return self.title