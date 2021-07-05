from django.db import models

# Create your models here.

class Disco(models.Model):
    id      = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=99)
    fecha   = models.DateField()

class Cancion(models.Model):
    id       = models.AutoField(primary_key=True)
    nombre   = models.CharField(max_length=99, default='')
    artista  = models.CharField(max_length=99)
    disco    = models.ForeignKey(Disco, on_delete=models.CASCADE)
    duracion = models.IntegerField()
