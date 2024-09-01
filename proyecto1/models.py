from typing import Any
from django.db import models


# Create your models here.
# los modelos son clases o entidades que representan las tablas de la base de datos

# Se crea la clase Libro que hereda de models.Model
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    autor = models.CharField(max_length=100, verbose_name='Autor')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen')
    descripcion = models.TextField(verbose_name='Descripción', null=True)

    # Se sobreescribe el método __str__ para que muestre el título y la descripción del libro
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - Descripción: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()