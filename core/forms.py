from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Genero, Usuario

class UsuarioForm(forms.ModelForm):
    

    class Meta:
        model = Usuario
        fields=['rut', 'nombre', 'apellido', 'genero', 'imagen']
        labels={
            'rut': 'Rut',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'genero': 'Genero',
            'imagen': 'Imagen',
        }
        widgets={
            'rut': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el RUT',
                    'id': 'rut', 
                }
            ),

            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ingrese el apellido',
                    'id': 'apellido'
                }
            ),
            'genero': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'id': 'genero'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen',
                }
            )
        }
