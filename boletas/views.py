from django.shortcuts import render, redirect
from boletas.models import Boleta
from .forms import BoletaForm

# Función para Listar Boletas
def crud_boletas(request):
    boletas = Boleta.objects.all()
    context = {'boletas': boletas}
    return render(request, "boletas/boletas_list.html", context)

# Función para Agregar Boletas
def boletas_ag(request):
    if request.method == 'POST':
        form = BoletaForm(request.POST)
        print(request.POST)  # Agrega esta línea para imprimir el contenido de request.POST
        if form.is_valid():
            form.save()
            return redirect('crud_boletas')
        else:
            print(form.errors)  # Agrega esta línea para imprimir los errores del formulario
    else:
        form = BoletaForm()

    return render(request, 'boletas_add.html', {'form': form})



# Función para Eliminar Boletas
def boletas_del(request, pk):
    mensajes=[]
    errores=[]
    boletas = Boleta.objects.all()
    try:
        boleta = Boleta.objects.get(id_boleta=pk)
        context={}
        if boleta:
            boleta.delete()
            mensajes.append("Perfecto! Datos eliminados")
            context = {'boletas':boletas, 'mensajes':mensajes, 'errores':errores}
            return render(request, "boletas/boletas_list.html", context)
        else:
            context={}
            return render(request, "boletas/boletas_list.html", context)
    except:
        print("Lo sentimos! No existe tal boleta")
        boletas=Boleta.objects.all()
        mensaje="Lo sentimos! No existe tal boleta"
        context={'mensaje':mensaje, 'boletas':boletas}
        return render (request, "boletas/boletas_list.html", context)
    
# Función1 para Editar Boletas
def boletas_edit(request, pk):
    if pk != "":
        boleta=Boleta.objects.get(id_boleta=pk)
        context={'boleta':boleta}
        if boleta:
            return render(request, "boletas/boletas_edit.html", context)
        else:
            context={'mensaje':"Lo lamentamos, no existe tal boleta."}
            return render(request, "boletas/boletas_list.html", context)
    else:
        context={}
        return render(request, "boletas/boletas_list.html", context)
    
# Función2 para Editar Boletas   
def boletasUpdate(request, pk):
    boleta = Boleta.objects.get(id_boleta=pk)  # Obtener la instancia existente

    if request.method == "POST":
        fecha = request.POST["fecha"]
        cliente = request.POST["cliente"]
        nombre = request.POST["nombre"]
        producto = request.POST["producto"]
        total = request.POST["total"]
        metodo_pago = request.POST["metodo_pago"]
        estado = request.POST["estado"]

        # Actualizar los campos de la instancia existente
        boleta.fecha = fecha
        boleta.cliente = cliente
        boleta.nombre = nombre
        boleta.producto = producto
        boleta.estado = estado
        boleta.total = total
        boleta.metodo_pago = metodo_pago

        boleta.save()

        context = {'mensaje': "Perfecto! Datos actualizados exitosamente", 'boleta': boleta}
        return render(request, "boletas/boletas_list.html", context)
    else:
        context = {}
        return render(request, "boletas/boletas_list.html", context)