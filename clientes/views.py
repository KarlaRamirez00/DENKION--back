from django.shortcuts import render
from clientes.models import Cliente

# Create your views here.

def crud(request):
    clientes = Cliente.object.all()
    context = {'clientes': clientes}
    return render(request, 'clientes/clientes_list', context)
