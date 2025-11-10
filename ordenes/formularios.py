from django import forms
from .models import Orden
from productos.models import Producto

class OrdenForm(forms.ModelForm):
    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Selecciona productos"
    )

    class Meta:
        model = Orden
        fields = ['productos']

class AgregarProductoForm(forms.Form):
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        label="Producto",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    cantidad = forms.IntegerField(
        min_value=1,
        label="Cantidad",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'})
    )
