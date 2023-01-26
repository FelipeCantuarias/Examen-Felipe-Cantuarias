from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm



# Create your views here.

def home(request):
    return render(request, 'index.html')

def galeria(request):
    return render(request, 'galeria.html')

def somos(request):
    return render(request, 'Somos.html')

def conta(request):
    return render(request, 'contactanos.html')

def api(request):
    return render(request, 'ApiRest.html')


def mostrar(request):
    usuarios = Usuario.objects.all()

    datos={
        'personas':usuarios
    }
    return render(request, 'mostrar.html', datos)

def eliminar(request, id):
    usuario = Usuario.objects.get(rut=id)
    usuario.delete()
    return redirect('mostrar')

def crear(request):
    if request.method=='POST':
        usuarioform = UsuarioForm(request.POST, request.FILES)
        if usuarioform.is_valid():
            usuarioform.save()
            return redirect('mostrar')
    else:
        usuarioform=UsuarioForm()
    return render(request, 'crearCliente.html', {'usuarioform': usuarioform})

def modificar(request, id):
    usuario = Usuario.objects.get(rut=id)
    datos = {
        'form': UsuarioForm(instance=usuario)
    }

    if request.method=='POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')

    return render(request, 'modificar.html', datos)