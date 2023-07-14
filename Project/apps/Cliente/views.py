from django.shortcuts import render, redirect
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
        if form.is_valid():
            form.save()
            return redirect("Cliente:clientes")
    else:
        form = ClienteForm()

    return render(request, "cliente/crear_clientes.html", {"form": form})

def busqueda(request):
    form = BusquedaForm()

    if request.method == "POST":
        form = BusquedaForm(request.POST)
        if form.is_valid():
            nombre_cliente = form.cleaned_data.get("nombre")
            return redirect("Cliente:resultados", nombre=nombre_cliente)

    return render(request, "cliente/buscar.html", {"form": form})

def resultados(request, nombre):
    listado_clientes = []

    if nombre:
        listado_clientes = Cliente.objects.filter(nombre__icontains=nombre)

    return render(request, "cliente/resultado_busqueda.html", {"resultado": listado_clientes})