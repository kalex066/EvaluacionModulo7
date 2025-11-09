from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, DetalleProducto
from .formularios import ProductoForm, DetalleProductoForm

#Vista para la pagina de Bienvenida
def index(request):
    return render(request, 'index.html')

#Vista para mostrar la lista de productos

def lista_productos(request):
    productos = Producto.objects.all() 
    return render(request, 'lista_productos.html', {"productos": productos})

# CRUD DE PRODUCTOS

def crear_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        detalle_form = DetalleProductoForm(request.POST)
        if producto_form.is_valid() and detalle_form.is_valid():
            producto = producto_form.save()
            detalle = detalle_form.save(commit=False)
            detalle.producto = producto
            detalle.save()
            return redirect('lista_productos')
    else:
        producto_form = ProductoForm()
        detalle_form = DetalleProductoForm()
    
    return render(request, 'crear_producto.html', {
        'producto_form': producto_form,
        'detalle_form': detalle_form
    })
#Update producto
def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    try:
        detalle = producto.detalleproducto
    except DetalleProducto.DoesNotExist:
        detalle = None

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, instance=producto)
        detalle_form = DetalleProductoForm(request.POST, instance=detalle)
        if producto_form.is_valid() and detalle_form.is_valid():
            producto = producto_form.save()
            detalle = detalle_form.save(commit=False)
            detalle.producto = producto
            detalle.save()
            return redirect('lista_productos')
    else:
        producto_form = ProductoForm(instance=producto)
        detalle_form = DetalleProductoForm(instance=detalle)

    return render(request, 'crear_producto.html', {
        'producto_form': producto_form,
        'detalle_form': detalle_form
    })

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=id)
    detalle = getattr(producto, 'detalleproducto', None)
    etiquetas = producto.etiquetas.all()

    return render(request, 'ver_producto.html', {
        'producto': producto,
        'detalle': detalle,
        'etiquetas': etiquetas
    })

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')

    return render(request, 'eliminar_producto.html', {
        'producto': producto
    })


