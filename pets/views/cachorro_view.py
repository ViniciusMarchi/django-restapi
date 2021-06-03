from ..models import Cachorro
from ..serializers import CachorroSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Metodos HTTP: GET, POST
class CachorrosView(APIView):
    # retorna todos os cachorros
    def get(self, request, format=None):
        try:
            cachorros = Cachorro.objects.all()
            serializer = CachorroSerializer(cachorros, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    # realize um post para os cachorros
    def post(self, request, format=None):
        serializer = CachorroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# metodos HTTP: GET, PUT (UPDATE), DELETE
class CachorroView(APIView):
    # verifica se o cliente existe, caso não existir, retorna HTTP 404 Not Found
    def get_valid_object(self, pk):
        try:
            return Cachorro.objects.get(pk=pk)
        except Cachorro.DoesNotExist:
            raise Http404
    
    
    
    
    # retorna um cachorro especifico
    def get(self, request, pk, format=None):
        cachorro = self.get_valid_object(pk)
        serializer = CachorroSerializer(cachorro)
        return Response(serializer.data)

    # UPDATE
    def put(self, request, pk, format=None):
        cachorro = Cachorro.objects.get(pk=pk)
        serializer = CachorroSerializer(cachorro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # deleta um cachorro do banco
    def delete(self, request, pk, foramt=None):
        cachorro = Cachorro.objects.get(pk=pk)
        cachorro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
