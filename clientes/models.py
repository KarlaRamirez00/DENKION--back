from django.db import models
from productos.models import Producto #OJO, esto es importante, y me había olvidado ponerlo

# Create your models here.

class Cliente(models.Model):
    rut               = models.IntegerField(primary_key=True)
    dv                = models.CharField(max_length=1, blank=False, null=False)
    nombre            = models.CharField(max_length=20, blank=False, null=False)
    apellido_paterno  = models.CharField(max_length=20, blank=False, null=False)
    apellido_materno  = models.CharField(max_length=20, blank=False, null=False)
    fec_nac           = models.DateField(blank=False, null=False)  
    telefono          = models.IntegerField(blank=False, null=False)
    direccion         = models.CharField(max_length=100, blank=False, null=False)
    comuna            = models.CharField(max_length=30, blank=False, null=False)
    ciudad            = models.CharField(max_length=30, blank=False, null=False)
    region            = models.CharField(max_length=30, blank=False, null=False)
    correo            = models.EmailField(unique=True, max_length=50, blank=True, null=True)
    contrasena        = models.CharField(max_length=15, blank=False, null=False)
    #id_producto       = models.ForeignKey('productos.Producto', on_delete=models.CASCADE, db_column='idProducto')


def __str__(self):
        return str(self.rut)+" "+str(self.nombre)+" "+str(self.apellido_paterno)+" "+str(self.apellido_materno)