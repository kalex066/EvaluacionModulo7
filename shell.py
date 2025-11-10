#Consultas ORM
from productos.models import Producto, Categoria, Etiqueta
#PRoductos con precio mayor a 25
productos_caros = Producto.objects.filter(precio__gt=25)

#Productos con etiqueta de zapatillas
productos_etiqueta_zapatillas = Producto.objects.filter(etiquetas='zapatillas')

#Contar productos por Categoria
from django.db.models import Count

categorias_con_conteo = Categoria.objects.annotate(total_productos=Count('producto'))

#Productos de color negro
productos_negros = Producto.objects.filter(detalle__color='negro')

#Productos con mas de una etiqueta
from django.db.models import Count

productos_varias_etiquetas = Producto.objects.raw("""
    SELECT productos_producto.id, productos_producto.nombre, COUNT(productos_producto_etiquetas.etiqueta_id) AS total_etiquetas
    FROM productos_producto
    JOIN productos_producto_etiquetas
        ON productos_producto.id = productos_producto_etiquetas.producto_id
    GROUP BY productos_producto.id, productos_producto.nombre
    HAVING COUNT(productos_producto_etiquetas.etiqueta_id) > 1
""")