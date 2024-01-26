from django.shortcuts import render
from productos.models import Producto

# Create your views here.

def crud(request):
    productos = Producto.object.all()
    context = {'productos': productos}
    return render(request, 'productos/productos_list', context)