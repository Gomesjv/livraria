from rest_framework.viewsets import ModelViewSet

from livraria.models import Usuario
from livraria.serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer