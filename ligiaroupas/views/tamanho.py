from rest_framework.viewsets import ModelViewSet

from ligiaroupas.models import Tamanho
from ligiaroupas.serializers import TamanhoSerializer

class TamanhoViewset(ModelViewSet):
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializer