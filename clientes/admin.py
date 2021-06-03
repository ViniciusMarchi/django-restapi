from django.contrib import admin
from .models import Cliente, Endereco

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'rg', 'telefone', 'email')
    base_model = Cliente

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('estado', 'cidade', 'bairro', 'numero', 'cep')
    base_model = Endereco