from django.contrib import admin
from .models import Cliente, Pais, Suscripcion
# Register your models here.

admin.site.register(Pais)
admin.site.register(Cliente)
admin.site.register(Suscripcion)
