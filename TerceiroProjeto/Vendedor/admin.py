from django.contrib import admin
from .models import Vendedor

@admin.register(Vendedor)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'data_nascimento', 'sexo', 'ativo', 'criado_em', 'atualizado_em')
    search_fields = ('nome', 'email')