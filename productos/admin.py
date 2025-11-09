from django.contrib import admin

from .models import Producto, DetalleProducto

class PerfilInline(admin.StackedInline):
    model = DetalleProducto
    can_delete = False
    verbose_name_plural = 'Detalle'

@admin.register(Producto)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio')
    inlines = (PerfilInline,)

@admin.register(DetalleProducto)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'peso', 'color')
