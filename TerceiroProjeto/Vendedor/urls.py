from django.urls import path
from . import views

urlpatterns = [
    path('Cliente/', views.listar_clientes, name='listar_clientes'),
]