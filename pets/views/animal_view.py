from ..models import Animal
from ..serializers import ProjectPolymorphicSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


# https://docs.djangoproject.com/en/3.2/topics/db/queries/



# https://www.django-rest-framework.org/tutorial/3-class-based-views/


# Metodo HTTP GET
class AnimaisView(APIView):
    # retorna todos os objetos do tipo Animal contidos no banco
    def get(self, request, format=None):
        try:
            animais = Animal.objects.all()
            serializer = ProjectPolymorphicSerializer(animais, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

# Metodo HTTP GET para um Animal especifico identificado por sua primary key
class AnimalView(APIView):
     # verifica se o cliente existe, caso não existir, retorna HTTP 404 Not Found
    def get_valid_object(self, pk):
        try:
            return Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            raise Http404    
    
    def get(self, request, pk, format=None):
        animal = self.get_valid_object(pk)
        serializer = ProjectPolymorphicSerializer(animal)
        return Response(serializer.data)
