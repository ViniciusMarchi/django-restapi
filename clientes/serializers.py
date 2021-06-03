from rest_framework import serializers
from .models import Cliente, Endereco

class EnderecoSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Endereco
        fields = '__all__'
        
        
class ClienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = Cliente
        fields = '__all__'