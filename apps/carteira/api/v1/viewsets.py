from rest_framework import viewsets
from apps.carteira.models import Carteira
from .serializers import CarteiraSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class CarteiraViewsets(viewsets.ModelViewSet):
    queryset = Carteira.objects.all()
    serializer_class = CarteiraSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
