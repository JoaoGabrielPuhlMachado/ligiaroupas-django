from rest_framework.viewsets import ModelViewSet

from ligiaroupas.models import Marca
from ligiaroupas.serializers import MarcaSerializer

class MarcaViewset(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer