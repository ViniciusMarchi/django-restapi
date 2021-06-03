from ..models import Veterinario
from ..serializers import VeterinarioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Metodos HTTP: GET, POST
class VeterinariosView(APIView):
    def get(self, request, format=None):
        try:
            veterinarios = Veterinario.objects.all()
            serializer = VeterinarioSerializer(veterinarios, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

    def post(self, request, format=None):
        serializer = VeterinarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# metodos HTTP: GET, PUT (UPDATE), DELETE
class VeterinarioView(APIView):
    # verifica se o cliente existe, caso não existir, retorna HTTP 404 Not Found
    def get_valid_object(self, pk):
        try:
            return Veterinario.objects.get(pk=pk)
        except Veterinario.DoesNotExist:
            raise Http404
    
    
    def get(self, request, pk, format=None):
        veterinario = self.get_valid_object(pk)
        serializer = VeterinarioSerializer(veterinario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        veterinario = Veterinario.objects.get(pk=pk)
        serializer = VeterinarioSerializer(veterinario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, foramt=None):
        veterinario = Veterinario.objects.get(pk=pk)
        veterinario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
