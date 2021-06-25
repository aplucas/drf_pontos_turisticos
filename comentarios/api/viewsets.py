from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from comentarios.models import Comentario
from comentarios.api.serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    authentication_classes = (BasicAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer