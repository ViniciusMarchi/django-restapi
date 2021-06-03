from rest_framework import serializers
from .models import Consulta

from clientes.serializers import ClienteSerializer
from pets.serializers import AnimalSerializer
from veterinarios.serializers import VeterinarioSerializer

class ConsultaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    animal = AnimalSerializer()
    veterinario = VeterinarioSerializer()
    
    class Meta:
        model = Consulta
        fields = '__all__'