from rest_framework.viewsets import ModelViewSet

from ligiaroupas.models import Cor
from ligiaroupas.serializers import CorSerializer

class CorViewset(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer