from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    
    def __str__(self):
        return self.nombre

class DetalleProducto(models.Model):
    producto = models.OneToOneField(  #Relacion one to one entre producto y detalle de producto
        Producto,
        on_delete = models.CASCADE,
        related_name = 'detalle'
    )
    peso = models.DecimalField(max_digits=4, decimal_places=2)
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Detalle de {self.producto.nombre}"
