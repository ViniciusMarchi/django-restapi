from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from ..models import Endereco
from ..serializers import EnderecoSerializer

# Metodos HTTP: GET, POST
class EnderecosView(APIView):
    def get(self, request, format=None):
        try:
            enderecos = Endereco.objects.all()
            serializer = EnderecoSerializer(enderecos, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def post(self, request, format=None):
        serializer = EnderecoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# metodos HTTP: GET, PUT (UPDATE), DELETE
class EnderecoView(APIView):
    # verifica se o cliente existe, caso não existir, retorna HTTP 404 Not Found
    def get_valid_object(self, pk):
        try:
            return Endereco.objects.get(pk=pk)
        except Endereco.DoesNotExist:
            raise Http404
    
    # GET
    def get(self, request, pk, format=None):
        endereco = self.get_valid_object(pk)
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)

    # UPDATE
    def put(self, request, pk, format=None):
        endereco = Endereco.objects.get(pk=pk)
        serializer = EnderecoSerializer(endereco, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def delete(self, request, pk, foramt=None):
        endereco = Endereco.objects.get(pk=pk)
        endereco.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
