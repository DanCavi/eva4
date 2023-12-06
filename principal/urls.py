from rest_framework import routers
from .api import PeliculaViewSet

router = routers.DefaultRouter()

router.register('api/principal', PeliculaViewSet, 'principal')

urlpatterns = router.urls


