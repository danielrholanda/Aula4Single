from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Vendedor

def listar_clientes(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    clientes = Vendedor.objects.all().order_by("nome").values("rg","nome","email","ativo")
    return JsonResponse(list(clientes), safe=False)