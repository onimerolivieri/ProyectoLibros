from django import forms
from .models import Libro

# Se crea la clase LibroForm que hereda de forms.ModelForm para crear un formulario de libros
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__' # Se obtienen todos los campos del modelo Libro