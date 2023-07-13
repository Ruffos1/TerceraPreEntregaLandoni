from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date
from .models import Cliente
from .forms import ClienteForm, BusquedaForm

# Create your views here.
def index(request):
    clientes_registros = Cliente.objects.all() 
    """Esta funcion muestra los objetos de un modelo"""
    contexto = {"Clientes": clientes_registros}
    return render(request, "cliente/index.html", context=contexto)

def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        #Indiaca que esta variable debe guardarse
        if form.is_valid():
            form.save()
            return redirect("Cliente:clientes")
    else: #request.method == "GET"
        form = ClienteForm()

    return render(request, "cliente/crear_clientes.html", context= {"form": form})

def busqueda(request: HttpRequest) -> HttpResponse:
    nombre_cliente = request.GET.get("nombre")
    if nombre_cliente:
        listado_clientes = Cliente.objects.filter(nombre__icontains = nombre_cliente)
        return render(request, "cliente/resultado_busqueda.html", {"resultado":listado_clientes})
    else:
        form = BusquedaForm()
        return render(request, "cliente/buscar.html", {"buscar":form})