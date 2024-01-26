from django.shortcuts import render
from boletas.models import Boleta

# Create your views here.

def crud(request):
    boletas = Boleta.object.all()
    context = {'boletas': boletas}
    return render(request, 'boletas/boletas_list', context)