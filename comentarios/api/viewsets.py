from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from comentarios.api.serializers import ComentarioSerializer
from comentarios.models import Comentario


class ComentarioViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication, ]
    permission_classes = (IsAuthenticated,)
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
