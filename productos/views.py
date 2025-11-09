from django.shortcuts import render, redirect
from .models import Producto, DetalleProducto

#Vista para la pagina de Bienvenida
def index(request):
    return render(request, 'index.html')

#Vista para mostrar la lista de productos

def lista_productos(request):
    productos = Producto.objects.all() 
    return render(request, 'lista_productos.html', {"productos": productos})

# Create your views here.
