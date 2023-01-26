from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Genero(models.Model):
    idGenero = models.IntegerField(primary_key=True, verbose_name='Genero Id')
    nombreGenero = models.CharField(max_length=30, verbose_name='Genero')

    def __str__(self):
        return self.nombreGenero


class Usuario(models.Model):
    rut=models.CharField(max_length=15, primary_key=True, verbose_name='Rut')
    nombre=models.CharField(max_length=20, verbose_name='Nombre')
    apellido=models.CharField(max_length=20, verbose_name='Apellido')
    imagen=models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut