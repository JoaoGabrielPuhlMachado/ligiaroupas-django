from rest_framework.serializers import ModelSerializer

from ligiaroupas.models import Tamanho

class TamanhoSerializer(ModelSerializer):
    class Meta:
        model = Tamanho
        fields = "__all__"