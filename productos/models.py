from django.db import models

class Categoria(models.Model):
    nombre = models.CharField (max_length = 100)
    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    etiquetas = models.ManyToManyField(Etiqueta)
    
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
        return self.producto.nombre

