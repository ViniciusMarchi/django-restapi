from django.urls import path
from clientes.views.cliente_view import ClientesView, ClienteView
from clientes.views.endereco_view import EnderecosView, EnderecoView

urlpatterns = [
    path('clientes/', ClientesView.as_view()),
    path('clientes/<int:pk>', ClienteView.as_view()),
    path('enderecos/', EnderecosView.as_view()),
    path('enderecos/<int:pk>', EnderecoView.as_view()),
]
