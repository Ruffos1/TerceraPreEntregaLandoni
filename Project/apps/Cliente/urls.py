from django.urls import path
from .views import index, crear_cliente, busqueda 

app_name = "Cliente"

urlpatterns = [
    path('',index, name="clientes" ),
    path("crear_cliente", crear_cliente, name="crear_cliente"),
    path("buscar/", busqueda, name="buscar")
]