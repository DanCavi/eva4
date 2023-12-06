from rest_framework import viewsets, permissions
from principal.models import Pelicula
from .serializers import PeliculaSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PeliculaSerializer

