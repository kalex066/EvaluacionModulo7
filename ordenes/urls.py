# ordenes/urls.py
from django.urls import path
from .views import ProductoClientesListView, CrearOrdenListadoView, OrdenListView, OrdenDetailView, guardar_orden, redireccion_post_login

app_name = 'ordenes'

urlpatterns = [
    path('redirigir/', redireccion_post_login, name='redireccion_post_login'),
    path('productos_clientes/', ProductoClientesListView.as_view(), name='lista_productos_clientes'),
    path('crear/', CrearOrdenListadoView.as_view(), name='crear_orden_listado'),
    path('guardar-orden/', guardar_orden, name='guardar_orden'),
    path('mis-ordenes/', OrdenListView.as_view(), name='lista_ordenes'),
    path('detalle/<int:pk>/', OrdenDetailView.as_view(), name='detalle_orden'),
]