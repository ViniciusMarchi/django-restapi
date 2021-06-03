from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from ..models import Cliente
from ..serializers import ClienteSerializer


# Metodos HTTP: GET, POST
class ClientesView(APIView):
    def get(self, request, format=None):
        try:
            clientes = Cliente.objects.all()
            serializer = ClienteSerializer(clientes, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# metodos HTTP: GET, PUT (UPDATE), DELETE
class ClienteView(APIView):
    
    # verifica se o cliente existe, caso não existir, retorna HTTP 404 Not Found
    def get_valid_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404
    
    # GET
    def get(self, request, pk, format=None):
        cliente = self.get_valid_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    # UPDATE
    def put(self, request, pk, format=None):
        cliente = Cliente.objects.get(pk=pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk, foramt=None):
        cliente = Cliente.objects.get(pk=pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
