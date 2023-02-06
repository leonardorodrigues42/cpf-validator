from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from django.http import QueryDict

from datetime import datetime

from .validator import Validator
from .models import Client
from .utils import format_date


class ClientSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "cpf",
            "birth",
            "created_at",
        ]
        read_only_fields = ["created_at"]
        
    def validate_cpf(self, cpf):
        validator = Validator()
        cpf = validator.validate(cpf)
        
        return cpf
    
    def validate_birth(self, birth):
        if birth > datetime.today().date():
            raise ValidationError("Data inválida")
        return birth
    
    def to_internal_value(self, data):
        if isinstance(data, QueryDict):
            data = data.dict()
            format_date(data)        
        
        return super().to_internal_value(data)
        
    