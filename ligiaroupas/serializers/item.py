from rest_framework.serializers import ModelSerializer

from ligiaroupas.models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class ItemDetailSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        depth = 1

class ItemListSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "nome", "preco"]