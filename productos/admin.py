from django.contrib import admin

from .models import Producto, DetalleProducto, Categoria, Etiqueta

class PerfilInline(admin.StackedInline):
    model = DetalleProducto
    can_delete = False
    verbose_name_plural = 'Detalle'

@admin.register(Producto)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'categoria')
    inlines = (PerfilInline,)
    filter_horizontal = ('etiquetas',)
    list_filter = ('categoria',)


@admin.register(DetalleProducto)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'peso', 'color')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
