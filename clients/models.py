from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=64)
    cpf = models.CharField(max_length=14, unique=True)
    birth = models.DateField(null=False)
    created_at = models.DateField(auto_now_add=True)
