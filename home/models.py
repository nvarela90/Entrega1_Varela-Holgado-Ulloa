from django.db import models
from ckeditor.fields import RichTextField

class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    descripcion = RichTextField(null = True)
    autor = models.CharField(max_length=30, null = True)
    imagen = models.ImageField(upload_to='jugadores', null = True, blank = True)
