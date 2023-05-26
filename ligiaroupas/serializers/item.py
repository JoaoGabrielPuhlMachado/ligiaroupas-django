from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer
from ligiaroupas.models import Item

class ItemSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Item
        fields = "__all__"

class ItemDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    class Meta:
        model = Item
        fields = "__all__"

class ItemListSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        depth = 1