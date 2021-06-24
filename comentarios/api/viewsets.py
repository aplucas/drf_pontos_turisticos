from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from comentarios.models import Comentario
from comentarios.api.serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer