from rest_framework.viewsets import ModelViewSet

from ligiaroupas.models import Categoria
from ligiaroupas.serializers import CategoriaSerializer

class CategoriaViewset(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer