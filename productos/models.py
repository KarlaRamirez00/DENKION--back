from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto     = models.AutoField(db_column='id_producto', primary_key=True)
    modelo          = models.CharField(max_length=20, blank=False, null=False)
    marca           = models.CharField(max_length=20, blank=False, null=False)
    anno_fab        = models.IntegerField(blank=False, null=False)
    precio          = models.IntegerField(blank=False, null=False)
    stock           = models.IntegerField(blank=False, null=False) 
    estado_choices  = [
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
    ]
    estado          = models.CharField(max_length=5, choices=estado_choices, blank=False, null=False)
    categoria       = models.CharField(max_length=20, blank=False, null=False)
    descripcion     = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.marca)+" "+str(self.modelo)+" "+str(self.anno_fab)
    

    class Cliente(models.Model):
        rut               = models.IntegerField(max_length=8, primary_key=True)
        dv                = models.CharField(max_length=1, blank=False, null=False)
        nombre            = models.CharField(max_length=20, blank=False, null=False)
        apellido_paterno  = models.CharField(max_length=20, blank=False, null=False)
        apellido_materno  = models.CharField(max_length=20, blank=False, null=False)
        fec_nac           = models.DateField(blank=False, null=False)  
        telefono          = models.IntegerField(max_length=8, blank=False, null=False)
        direccion         = models.CharField(max_length=100, blank=False, null=False)
        comuna            = models.CharField(max_length=30, blank=False, null=False)
        ciudad            = models.CharField(max_length=30, blank=False, null=False)
        region            = models.CharField(max_length=30, blank=False, null=False)
        correo            = models.EmailField(unique=True, max_length=50, blank=True, null=True)
        contrasena        = models.CharField(max_length=15, blank=False, null=False)
        id_producto       = models.ForeignKey('Producto', on_delete=models.CASCADE, db_column='idProducto')



    def __str__(self):
        return str(self.rut)+" "+str(self.mnombre)+" "+str(self.apellido_paterno)+" "+str(self.apellido_materno)+" "+str(self.id_producto)