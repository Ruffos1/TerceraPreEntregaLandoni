from django.urls import path
from .views import index

app_name = "Cliente"

urlpatterns = [
    path('',index, name="clientes" ),
]