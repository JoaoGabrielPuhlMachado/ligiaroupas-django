from rest_framework.viewsets import ModelViewSet

from ligiaroupas.models import Item
from ligiaroupas.serializers import ItemSerializer, ItemDetailSerializer, ItemListSerializer

class ItemViewset(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ItemListSerializer
        elif self.action == "retrieve":
            return ItemDetailSerializer
        return ItemSerializer