from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class CategoryDB(models.Model):
    name= models.CharField(max_length=100, verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta():
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering=["created"]
    

    def __str__(self):
        return self.name
    
class  PostDB(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image= models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author= models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories= models.ManyToManyField(CategoryDB, verbose_name="Categorias", related_name="get_posts")
    created= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update= models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta():
        verbose_name="Entrada"
        verbose_name_plural="Entradas"
        ordering=["created"]
    

    def __str__(self):
        return self.title