from rest_framework.viewsets import ModelViewSet

from ligiaroupas.models import Produto
from ligiaroupas.serializers import ProdutoSerializer, ProdutoDetailSerializer, ProdutoListSerializer

class ProdutoViewset(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer