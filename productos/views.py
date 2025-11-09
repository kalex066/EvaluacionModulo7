from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, DetalleProducto, Categoria, Etiqueta
from .formularios import ProductoForm, DetalleProductoForm, CategoriaForm, EtiquetaForm
from django.contrib import messages

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
        detalle = producto.detalle
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

def detalle_producto(request, id):
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


# CATEGORIAS CRUD
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {
        'categorias': categorias
    })

def crear_categorias(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoría creada exitosamente.')
        return redirect('lista_categorias')
    return render(request, 'form_categoria.html', {
        'form': form,
        'titulo': 'Crear categoría'
    })

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoría actualizada correctamente.')
        return redirect('lista_categorias')
    return render(request, 'form_categoria.html', {
        'form': form,
        'titulo': 'Editar categoría'
    })

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada correctamente.')
        return redirect('lista_categorias')
    return render(request, 'eliminar_categoria.html', {
        'categoria': categoria
    })

#ETIQUETAS CRUD
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'lista_etiquetas.html', {
        'etiquetas': etiquetas
    })

def crear_etiqueta(request):
    form = EtiquetaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Etiqueta creada exitosamente.')
        return redirect('lista_etiquetas')
    return render(request, 'form_etiqueta.html', {
        'form': form,
        'titulo': 'Crear etiqueta'
    })

def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, pk=id)
    form = EtiquetaForm(request.POST or None, instance=etiqueta)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Etiqueta actualizada correctamente.')
        return redirect('lista_etiquetas')
    return render(request, 'form_etiqueta.html', {
        'form': form,
        'titulo': 'Editar etiqueta'
    })

def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, pk=id)
    if request.method == 'POST':
        etiqueta.delete()
        messages.success(request, 'Etiqueta eliminada correctamente.')
        return redirect('lista_etiquetas')
    return render(request, 'eliminar_etiqueta.html', {
        'etiqueta': etiqueta
    })