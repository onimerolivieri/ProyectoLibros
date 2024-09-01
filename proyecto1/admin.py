from django.contrib import admin
from .models import Libro # Se importa la clase Libro del archivo models.py

# Register your models here.

admin.site.register(Libro) # Se registra la clase Libro en el panel de administración
