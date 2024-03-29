from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraSerializer, CriarEditarCompraSerializer
from usuario.models import Usuario


def userIsAnonymous(user):
    return str(user) == "AnonymousUser"


class CompraViewset(ModelViewSet):
    queryset = Compra.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["usuario", "status", "data"]
    search_fields = ["usuario__email", "status"]
    ordering_fields = ["usuario", "status", "data"]
    ordering = ["usuario"]



    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        if usuario.tipo_usuario == Usuario.TipoUsuario.ADMIN:
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarCompraSerializer
        return CompraSerializer
    
    def list(self, request):
        usuario = self.request.user
        if userIsAnonymous(usuario):
            return Response({"message": "Usuário não autenticado"}, status=status.HTTP_403_FORBIDDEN)
        if self.queryset.count() == 0:
            data = "{}"
        else:
            data = self.get_serializer_class()(self.queryset.all).data
        return Response(data, status=status.HTTP_200_OK)
