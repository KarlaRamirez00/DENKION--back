from django.db import models
#OJO, hay que importar las clases de las cuales usaremos atributos como ForeignKey
from productos.models import Producto 
from clientes.models import Cliente 

# Create your models here.   
   
class Boleta(models.Model):
    id_boleta           = models.AutoField(db_column='id_boleta', primary_key=True)
    fecha               = models.DateField(blank=False, null=False)
    cliente             = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE, db_column='Rut')
    producto            = models.ForeignKey('productos.Producto', on_delete=models.CASCADE, db_column='id_producto')
    nombre              = models.CharField(max_length=20, blank=False, null=False)
    total               = models.IntegerField(blank=False, null=False)
    metodo_pago_choices = [
        ('efectivo', 'Efectivo'),
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
        ('transferencia', 'Transferencia'),
    ]
    metodo_pago         = models.CharField(max_length=15, choices=metodo_pago_choices)
    estado_choices      = [
    ('aprobado', 'Aprobado'),
    ('rechazado', 'Rechazado'),
    ]
    estado              = models.CharField(max_length=10, choices=estado_choices, blank=False, null=False)
    
def __str__(self):
        return str(self.id_boleta)+" "+str(self.fecha)+" "+str(self.cliente.rut)+" "+str(self.total)