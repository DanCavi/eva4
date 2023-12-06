from django.db import models

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    puntaje = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

