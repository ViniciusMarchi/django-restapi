from django.contrib import admin
from consultas.models import Consulta
from pets.models import Animal

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('animal', 'cliente', 'data_consulta', 'veterinario')
    base_model = Consulta
    readonly_fields=("cliente",)