from django.urls import path
from consultas.views.consulta_view import ConsultasView, ConsultaView

urlpatterns = [
    path('consultas/', ConsultasView.as_view()),
    path('consultas/<int:pk>', ConsultaView.as_view()),
]