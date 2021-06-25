from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from avaliacoes.api.serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication, ]
    permission_classes = (IsAuthenticated,)
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
