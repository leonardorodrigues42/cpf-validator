from rest_framework.exceptions import ValidationError
from .models import Client

import numpy as np


class Validator():
    def format_cpf(self, cpf):
        return cpf.replace(".", "").replace("-", "")
    
    
    def _length_validation(self, cpf):        
        cpf = self.format_cpf(cpf)
        
        if not cpf.isnumeric():
            raise ValidationError("O CPF deve conter apenas números")
        
        if len(cpf) != 11:
            raise ValidationError("O CPF deve conter 11 dígitos numéricos")
        
        return cpf
    
    
    def _check_if_cpf_exists(self, cpf):
        cpf = self._length_validation(cpf)
        
        client = Client.objects.filter(cpf=cpf).first()
        
        if client:
            raise ValidationError("Já existe um cliente com esse CPF cadastrado")
        
        return cpf
        
    
    def _validate_first_check_digit(self, cpf):
        cpf = self._check_if_cpf_exists(cpf)
        
        first_check_digit = int(cpf[9:10])
        
        multipliers  = [n for n in range(2, 11)][::-1]
        numbers_cpf  = [int(n) for n in cpf][0:9]
        
        multiplication = sum(np.multiply(multipliers, numbers_cpf))
        
        rest = multiplication % 11
        
        if rest < 2 and first_check_digit == 0:
            return cpf
        
        if (11 - rest) == first_check_digit:
            return cpf
        
        raise ValidationError("CPF inválido")
    
    
    def _validate_check_digits(self, cpf):
        cpf = self._validate_first_check_digit(cpf)
        
        last_check_digit = int(cpf[10:])
        
        multipliers  = [n for n in range(2, 12)][::-1]
        numbers_cpf  = [int(n) for n in cpf][0:10]
        
        multiplication = sum(np.multiply(multipliers, numbers_cpf))
        
        rest = multiplication % 11
        
        if rest < 2 and last_check_digit == 0:
            return cpf
        
        if (11 - rest) == last_check_digit:
            return cpf
        
        raise ValidationError("CPF inválido")
    
    
    def validate(self, cpf):
        cpf = self._validate_check_digits(cpf)
        
        return cpf
    