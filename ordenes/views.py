from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Orden, ProductoOrden
from .formularios import OrdenForm, AgregarProductoForm
from productos.models import Producto
from django.contrib import messages


@login_required
def redireccion_post_login(request):
    if request.user.is_staff:
        return redirect('lista_productos')
    else:
        return redirect('ordenes:lista_productos_clientes')

class ProductoClientesListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'lista_productos_clientes.html'
    context_object_name = 'productos_clientes'
    paginate_by = 5 

class CrearOrdenListadoView(TemplateView):
    template_name = 'crear_orden_listado.html'
    def get(self, request):
        form = AgregarProductoForm()
        carrito = request.session.get('carrito', [])
        productos = Producto.objects.filter(id__in=[p['id'] for p in carrito])
        return render(request, self.template_name, {'form': form, 'carrito': carrito, 'productos': productos})

    def post(self, request):
        form = AgregarProductoForm(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']
            carrito = request.session.get('carrito', [])

            # Evita duplicados
            if not any(p['id'] == producto.id for p in carrito):
                carrito.append({'id': producto.id, 'nombre': producto.nombre, 'cantidad': cantidad})
                request.session['carrito'] = carrito

        return redirect('ordenes:crear_orden_listado')

def guardar_orden(request):
    carrito = request.session.get('carrito', [])
    if not carrito:
        messages.warning(request, "No hay productos en la orden.")
        return redirect('ordenes:crear_orden')
    # Crear la orden
    orden = Orden.objects.create(usuario=request.user)

    # Agregar productos con cantidad
    for item in carrito:
        producto = Producto.objects.get(id=item['id'])
        cantidad = item['cantidad']
        ProductoOrden.objects.create(
            orden=orden,
            producto=producto,
            cantidad=cantidad
        )
    request.session['carrito'] = []

    messages.success(request, "Orden creada exitosamente.")
    return redirect('ordenes:lista_ordenes')

class OrdenListView(LoginRequiredMixin, ListView):
    model = Orden
    template_name = 'lista_ordenes.html'
    context_object_name = 'ordenes'

    def get_queryset(self):
        return Orden.objects.filter(usuario=self.request.user)

class OrdenDetailView(LoginRequiredMixin, DetailView):
    model = Orden
    template_name = 'detalle_orden.html'
    context_object_name = 'orden'

    def get_queryset(self):
        return Orden.objects.filter(usuario=self.request.user)
