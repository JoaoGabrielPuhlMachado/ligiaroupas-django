from rest_framework import serializers
from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField

from core.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItensCompra
        fields = ("produto","preco_item", "quantidade", "total")
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.produto.preco


class CompraSerializer(ModelSerializer):
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = CharField(source="get_status_display", read_only=True)
    data = serializers.DateTimeField(read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "data", "itens")

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return instance


class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade")

    def validate(self, data):
        if data["quantidade"] > data["produto"].quantidade:
            raise serializers.ValidationError({"quantidade": "Quantidade solicitada não disponível em estoque."})
        return data


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    data = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Compra
        fields = ("usuario","data", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            item["preco_item"] = item["produto"].preco
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                item["preco_item"] = item["produto"].preco
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return instance