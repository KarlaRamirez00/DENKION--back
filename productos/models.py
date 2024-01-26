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
    desc            = models.TextField(max_length=200, blank=False, null=False)

    def __str__(self):
        return str(self.marca)+" "+str(self.modelo)+" "+str(self.anno_fab)