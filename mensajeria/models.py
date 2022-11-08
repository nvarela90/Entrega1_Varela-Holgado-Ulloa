from django.db import models
from ckeditor.fields import RichTextField

class Mensaje(models.Model):
    texto = RichTextField(null = True)
    emisor = models.CharField(max_length = 30)
    receptor = models.CharField(max_length = 30)
