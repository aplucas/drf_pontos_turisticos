from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class EnderecoViewSet(ModelViewSet):
    authentication_classes = (BasicAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
