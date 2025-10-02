from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField()
    rg = models.CharField()
    email = models.EmailField()
    telefone = models.CharField()
    endereco = models.CharField()
    data_nascimento = models.DateTimeField()
    sexo = models.CharField()
    ativo = models.CharField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True) 