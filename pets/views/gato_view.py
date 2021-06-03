from ..models import Gato
from ..serializers import GatoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Metodos HTTP: GET, POST
class GatosView(APIView):

    # retorna todos os gatos
    def get(self, request, format=None):
        try:
            gatos = Gato.objects.all()
            serializer = GatoSerializer(gatos, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # adiciona diversos gatos de uma vez
    def post(self, request, format=None):
        serializer = GatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# metodos HTTP: GET, PUT (UPDATE), DELETE
class GatoView(APIView):
    
    # verifica se o cliente existe, caso não existir, retorna HTTP 404 Not Found
    def get_valid_object(self, pk):
        try:
            return Gato.objects.get(pk=pk)
        except Gato.DoesNotExist:
            raise Http404
    
    
    
    # retorna um gato especifico
    def get(self, request, pk, format=None):
        gato = self.get_valid_object(pk)
        serializer = GatoSerializer(gato)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        gato = Gato.objects.get(pk=pk)
        serializer = GatoSerializer(gato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, foramt=None):
        gato = Gato.objects.get(pk=pk)
        gato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
