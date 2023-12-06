from rest_framework import serializers
from .models import Pelicula

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ('id', 'nombre', 'genero', 'puntaje', 'created_at')
        read_only_fields = ('created_at',)

