from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "nacimiento", "pais_origen_id","plan_suscripcion"]
        "Valores que queremos visualizar"

class BusquedaForm(forms.Form):
    nombre = forms.CharField()