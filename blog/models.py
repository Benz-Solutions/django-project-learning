from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=75, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    user = models.ForeignKey(User, verbose_name="Autor", editable=False, on_delete=models.CASCADE)
    image = models.ImageField(default="null", verbose_name="Imagen")
    public = models.BooleanField(verbose_name="¿Publicado?")
    categories = models.ManyToManyField(Category, verbose_name="Categorías", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
    
    def __str__(self):
        return self.title