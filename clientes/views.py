from django.shortcuts import render, redirect
from clientes.models import Cliente
from django.contrib.auth.models import User
from .forms import ClienteForm

# Función para Listar Clientes
def crud_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, "clientes/clientes_list.html", context)

# Función para Agregar Clientes
def clientes_ag(request):
    if request.method == 'POST':
        # Crear una instancia del formulario con los datos del request
        form = ClienteForm(request.POST)

        # Verificar si el formulario es válido
        if form.is_valid():
            # Guardar el objeto Cliente en la base de datos
            cliente = form.save(commit=False)

            # Crear el usuario
            user = User.objects.create_user(username=cliente.correo, email=cliente.correo, password=cliente.contrasena)
            user.save()

            # Asignar el usuario al cliente
            cliente.usuario = user
            cliente.save()

            return redirect('crud_clientes')  # Redirigir a la lista de clientes

    else:
        # Si es una solicitud GET, simplemente mostrar el formulario en blanco
        form = ClienteForm()

    context = {'form': form}
    return render(request, 'clientes/clientes_add.html', context)
  
    
# Función para Eliminar Clientes
def clientes_del(request, pk):
    mensajes=[]
    errores=[]
    clientes = Cliente.objects.all()
    try:
        cliente = Cliente.objects.get(rut=pk)
        context={}
        if cliente:
            cliente.delete()
            mensajes.append("Perfecto! Datos eliminados")
            context = {'clientes':clientes, 'mensajes':mensajes, 'errores':errores}
            return render(request, "clientes/clientes_list.html", context)
        else:
            context={}
            return render(request, "clientes/clientes_list.html", context)
    except:
        print("Lo sentimos! No existe tal cliente")
        clientes=Cliente.objects.all()
        mensaje="Lo sentimos! No existe tal cliente"
        context={'mensaje':mensaje, 'clientes':clientes}
        return render (request, "clientes/clientes_list.html", context)
    
# Función1 para Editar Clientes
def clientes_edit(request, pk):
    if pk != "":
        cliente=Cliente.objects.get(rut=pk)
        context={'cliente':cliente}
        if cliente:
            return render(request, "clientes/clientes_edit.html", context)
        else:
            context={'mensaje':"Lo lamentamos, no existe tal cliente."}
            return render(request, "clientes/clientes_list.html", context)
    else:
        context={}
        return render(request, "clientes/clientes_list.html", context)
    
# Función2 para Editar Clientes   
def clientesUpdate(request):
    if request.method == "POST":
        rut=request.POST["rut"]
        dv=request.POST["dv"]
        nombre=request.POST["nombre"]
        apellido_paterno=request.POST["apellido_paterno"]
        apellido_materno=request.POST["apellido_materno"]
        fec_nac=request.POST["fec_nac"]
        telefono=request.POST["telefono"]
        direccion=request.POST["direccion"]
        comuna=request.POST["comuna"]
        ciudad=request.POST["ciudad"]           
        region=request.POST["region"]           
        correo=request.POST["correo"]            
        contrasena=request.POST["contrasena"]       
        id_producto=request.POST["id_producto"] 

        cliente = Cliente()
        cliente.rut = rut
        cliente.dv = dv
        cliente.nombre = nombre
        cliente.apellido_paterno = apellido_paterno
        cliente.apellido_materno = apellido_materno
        cliente.fec_nac = fec_nac
        cliente.telefono = telefono
        cliente.direccion = direccion
        cliente.comuna = comuna
        cliente.ciudad = ciudad
        cliente.region = region
        cliente.correo = correo
        cliente.contrasena = contrasena
        cliente.id_producto = id_producto
        cliente.save()
        context={'mensaje':"Perfecto! Datos actualizados exitosamente", 'cliente':cliente}
        return render(request, "clientes/clientes_list.html", context)
    else:
        context = {}
        return render(request, "clientes/clientes_list.html", context)