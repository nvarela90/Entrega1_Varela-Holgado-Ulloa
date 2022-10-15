from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
