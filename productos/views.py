from django.shortcuts import render
from productos.models import Producto
from .forms import ProductoForm

# Función para Listar Productos
def crud_productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, "productos/productos_list.html", context)


# Función para Agregar Productos
def productos_ag(request):
    context={}

    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            print ("estoy en si es válido")
            form.save()

            #limpiar form
            form = ProductoForm()

            context={'mensaje':"Perfecto! El producto ha sido guardado correctamente", "form":form}
            return render(request, "productos/productos_add.html", context)
    else:
        form = ProductoForm()
        context = {'form':form}
        return render (request, "productos/productos_add.html", context)
    
# Función para Eliminar Productos
def productos_del(request, pk):
    mensajes=[]
    errores=[]
    productos = Producto.objects.all()
    try:
        producto = Producto.objects.get(id_producto=pk)
        context={}
        if producto:
            producto.delete()
            mensajes.append("Perfecto! Datos eliminados")
            context = {'productos':productos, 'mensajes':mensajes, 'errores':errores}
            return render(request, "productos/productos_list.html", context)
        else:
            context={}
            return render(request, "productos/productos_list.html", context)
    except:
        print("Lo sentimos! No existe tal producto")
        productos=Producto.objects.all()
        mensaje="Lo sentimos! No existe tal producto"
        context={'mensaje':mensaje, 'productos':productos}
        return render (request, "productos/productos_list.html", context)
    
# Función1 para Editar Productos
def productos_edit(request, pk):
    if pk != "":
        producto=Producto.objects.get(id_producto=pk)
        context={'producto':producto}
        if producto:
            return render(request, "productos/productos_edit.html", context)
        else:
            context={'mensaje':"Lo lamentamos, no existe tal producto."}
            return render(request, "productos/productos_list.html", context)
    else:
        context={}
        return render(request, "productos/productos_list.html", context)
    

# Función2 para Editar Productos 
def productosUpdate(request, pk):
    errores = []  # Inicializa la variable

    try:
        producto = Producto.objects.get(id_producto=pk)
    except Producto.DoesNotExist:
        errores.append("Lo lamentamos, no existe tal producto.")
        productos = Producto.objects.all()
        context = {'productos': productos, 'errores': errores}
        return render(request, "productos/productos_list.html", context)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)

        if form.is_valid():
            form.save()
            mensajes = ["Perfecto! Datos actualizados exitosamente"]
            productos = Producto.objects.all()
            context = {'productos': productos, 'mensajes': mensajes}
            return render(request, "productos/productos_list.html", context)
        else:
            errores.append("Error en el formulario")
    else:
        errores.append("Error en la solicitud POST")

    # Asegúrate de que la variable 'productos' está definida antes de usarla en el contexto.
    productos = Producto.objects.all()
    context = {'productos': productos, 'errores': errores}
    return render(request, "productos/productos_list.html", context)