from rest_framework.routers import DefaultRouter
from apps.transacao.api.v1.viewsets import TransacaoViewsets

router = DefaultRouter()
router.register(r'transacoes', TransacaoViewsets)

urlpatterns = router.urls
