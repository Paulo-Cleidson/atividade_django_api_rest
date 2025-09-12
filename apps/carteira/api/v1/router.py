from rest_framework.routers import DefaultRouter
from apps.carteira.api.v1.viewsets import CarteiraViewsets

router = DefaultRouter()
router.register(r'carteiras', CarteiraViewsets)

urlpatterns = router.urls
