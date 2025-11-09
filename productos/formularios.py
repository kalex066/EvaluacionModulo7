from django import forms
from .models import Producto,DetalleProducto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']
        widgets = {
            'categoria': forms.Select(),
            'etiquetas': forms.CheckboxSelectMultiple()
        }

class DetalleProductoForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = ['peso', 'color']

