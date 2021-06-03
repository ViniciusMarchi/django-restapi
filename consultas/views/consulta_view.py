from consultas.models import Consulta
from consultas.serializers import ConsultaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pets.models import Animal
from django.http import Http404


# Metodos HTTP: GET, POST
class ConsultasView(APIView):
    def get(self, request, format=None):
        try:
            constulas = Consulta.objects.all()
            serializer = ConsultaSerializer(constulas, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

    def post(self, request, format=None):
        serializer = ConsultaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# metodos HTTP: GET, PUT (UPDATE), DELETE
class ConsultaView(APIView):
     # verifica se o cliente existe, caso não existir, retorna HTTP 404 Not Found
    def get_valid_object(self, pk):
        try:
            return Consulta.objects.get(pk=pk)
        except Consulta.DoesNotExist:
            raise Http404
    
    # GET
    def get(self, request, pk, format=None):
        consulta = self.get_valid_object(pk)
        serializer = ConsultaSerializer(consulta)
        return Response(serializer.data)

    # UPDATE
    def put(self, request, pk, format=None):
        consulta = Consulta.objects.get(pk=pk)
        serializer = ConsultaSerializer(consulta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk, foramt=None):
        consulta = Consulta.objects.get(pk=pk)
        consulta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    