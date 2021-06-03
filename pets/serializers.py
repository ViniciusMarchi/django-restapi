from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from .models import Animal, Cachorro, Gato, Passaro

# https://django-polymorphic.readthedocs.io/en/stable/third-party.html

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class CachorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cachorro
        fields = '__all__'


class GatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gato
        fields = '__all__'


class PassaroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passaro
        fields = '__all__'


class ProjectPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Animal: AnimalSerializer,
        Cachorro: CachorroSerializer,
        Gato: GatoSerializer,
        Passaro: PassaroSerializer
    }