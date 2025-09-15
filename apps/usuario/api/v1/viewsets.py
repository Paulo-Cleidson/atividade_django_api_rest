from rest_framework import viewsets
from apps.usuario.models import Usuario
from apps.usuario.api.v1.serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated


class UsuarioViewsets(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]
