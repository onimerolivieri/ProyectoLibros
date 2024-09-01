from django.urls import path 
from . import views # Se importan las vistas del archivo views.py
from django.conf import settings # Se importa settings para poder acceder a las variables de configuración
from django.contrib.staticfiles.urls import static # Se importa static para poder acceder a las imágenes


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('libros/', views.libros, name='libros'),
    path('libros/crear/', views.crear, name='crear'),
    path('libros/editar/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>/', views.editar, name='editar'),
    path('libros/buscar/', views.buscar, name='buscar'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Se añade la url de las imágenes
