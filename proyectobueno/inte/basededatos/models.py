from django.db import models

# Create your models here.
class Usuario(models.Model):
    user=models.CharField(max_length=8)
    pas=models.CharField(max_length=8)
    def __str__(self):
        return 'El usuario %s ya se encuentra registrado con la clave %s'%(self.user, self.pas)
        
class Infraccion(models.Model):
    folio=models.CharField(max_length=100)
    nombreinfractor=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    no_economico=models.CharField(max_length=50)
    ruta=models.CharField(max_length=50)
    lugar=models.CharField(max_length=50)
    fecha=models.DateField(max_length=50)
    hora=models.CharField(max_length=50)
    num_licencia=models.IntegerField()
    motivo=models.CharField(max_length=80)
    garantia=models.CharField(max_length=50)
    arti=models.IntegerField()
    matricula=models.CharField(max_length=50)
    cardcirculacion=models.CharField(max_length=50)
    user=models.CharField(max_length=8)

class Parquimetros(models.Model):
    foliopar=models.CharField(max_length=100)
    motivo=models.CharField(max_length=100)
    num_estacionamiento=models.CharField(max_length=50)
    manzana=models.CharField(max_length=50)
    sector=models.CharField(max_length=50)
    calle=models.CharField(max_length=50)
    vencimiento=models.CharField(max_length=50)
    nombreinfractor=models.CharField(max_length=50)
    matricula=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    num_permiso=models.IntegerField()
    marca=models.CharField(max_length=50)
    foliodepago=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    serie=models.CharField(max_length=50)
    user=models.CharField(max_length=8)


class Multas(models.Model):
    folio=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
