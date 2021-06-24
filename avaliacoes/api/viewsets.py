from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from avaliacoes.models import Avaliacao
from avaliacoes.api.serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer