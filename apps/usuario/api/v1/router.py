from rest_framework.routers import DefaultRouter
from apps.usuario.api.v1.viewsets import UsuarioViewsets

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewsets)

urlpatterns = router.urls
