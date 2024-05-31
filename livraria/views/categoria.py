from rest_framework.viewsets import ModelViewSet
from livraria.models import Categoria, Editora
from rest_framework.permissions import IsAuthenticated
from livraria.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]