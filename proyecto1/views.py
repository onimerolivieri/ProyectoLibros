from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from django.db.models import Q # Se importa la clase Q para realizar consultas más complejas
from .forms import LibroForm
from django.core.paginator import Paginator
# Create your views here. 

# Se crea la función inicio que recibe un request y retorna un render con el archivo inicio.html
def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def libros(request):
    query = request.GET.get('q')
    if query:
        libros_list = Libro.objects.filter(
            Q(titulo__icontains=query) | Q(autor__icontains=query)
        )
    else:
        libros_list = Libro.objects.all()
    
    paginator = Paginator(libros_list, 5)  # Muestra 5 libros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'libros/index.html', {'page_obj': page_obj})


"""def libros(request):
    libros_list = Libro.objects.all() # Se obtienen todos los libros de la base de datos
    paginator = Paginator(libros_list, 5)  # Muestra 5 libros por página
    page_number = request.GET.get('page') # Se obtiene el número de página actual 
    page_obj = paginator.get_page(page_number) # Se obtiene la página actual 
    return render(request, 'libros/index.html', {'page_obj': page_obj})

def libros(request):
   libros = Libro.objects.all() # Se obtienen todos los libros de la base de datos
   print(libros) # Se imprime en consola los libros para verificar que se obtuvieron correctamente
   return render(request, "libros/index.html", {'libros': libros}) # Se retorna un render con los libros obtenidos"""

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None) # Se crea un formulario de libros
    if formulario.is_valid(): # Se verifica si el formulario es válido
        formulario.save() # Se guarda el formulario
        return redirect('libros') # Se redirecciona a la vista de libros
    return render(request, "libros/crear.html", {'formulario': formulario}) # Se retorna un render con el formulario

def editar(request, id): # Se recibe el id del libro que se desea editar
    libro = Libro.objects.get(id=id) # Se obtiene el libro con el id que se recibe
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro) # Se crea un formulario de libros
    if formulario.is_valid() and request.POST: # Se verifica si el formulario es válido y si se ha enviado un POST
        formulario.save() # Se guarda el formulario
        return redirect('libros')
    return render(request, "libros/editar.html", {'formulario': formulario}) # Se retorna un render con el libro

def eliminar(request, id): # Se recibe el id del libro que se desea eliminar
    libro = Libro.objects.get(id=id) # Se obtiene el libro con el id que se recibe
    libro.delete() # Se elimina el libro
    return redirect('libros') 
    return render(request, "libros/eliminar.html")

def buscar(request):
    query = request.GET.get('q') 
    resultados = []
    if query:
        resultados = Libro.objects.filter(titulo__icontains=query)  
    return render(request, 'libros/buscar.html', {'resultados': resultados, 'query': query})

