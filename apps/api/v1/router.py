from rest_framework.routers import DefaultRouter
from .viewsets import CarteiraViewsets

router = DefaultRouter()
router.register(r'carteiras', CarteiraViewsets)

urlpatterns = router.urls
