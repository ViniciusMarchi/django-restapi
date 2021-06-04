from django.contrib import admin
from .models import Veterinario

@admin.register(Veterinario)
class VetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'crmv', 'especialidade')
    base_model = Veterinario