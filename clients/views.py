from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework import status

from .serializers import ClientSerializer
from .models import Client
from .validator import Validator


class ClientListCreateView(ListCreateAPIView):
    queryset = Client.objects.all().order_by("id")
    serializer_class = ClientSerializer     
    
    def handle_exception(self, exc):
        if isinstance(exc, ValidationError):
            if exc.detail["cpf"][0] == "CPF inválido":
                exc.status_code = status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            return Response(exc.detail, status=exc.status_code)
        return super().handle_exception(exc)
    

class ClientRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def get_object(self):
        cpf = self.kwargs.get("cpf")
        cpf = Validator.format_cpf(self, cpf)
        try:
            return self.queryset.get(cpf=cpf)
        except Client.DoesNotExist:
            raise NotFound(f'Não foi encontrado um client castrado com o CPF {cpf}')
        
