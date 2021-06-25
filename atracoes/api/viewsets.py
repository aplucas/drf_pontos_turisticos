from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao


class AtracaoViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication, ]
    permission_classes = (IsAuthenticated,)
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filterset_fields = ('nome', 'descricao')
