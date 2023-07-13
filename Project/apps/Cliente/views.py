from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date
from.models import Cliente
from .forms import ClienteForm

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

def Busqueda(request : HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            nacimiento = form.cleaned_data["nacimiento"]
            pais_origen_id = form.cleaned_data["pais_origen_id"]
            plan_suscripcion = form.cleaned_data["plan_suscripcion"]
            busqueda= Cliente.objects.filter(
                nombre__icontains = nombre,
                apellido__icontains = apellido,
                nacimiento__icontains = nacimiento,
                pais_origen_id__icontains = pais_origen_id,
                plan_suscripcion__icontains = plan_suscripcion,
            )
            return render(request, "resultado_busqueda.html", {"Resultado":busqueda})
        else:
            form = ClienteForm()
        return render(request, "buscar.html", {"buscar": form})
    