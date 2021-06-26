from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, ]
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao', 'endereco__linha1']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(id=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(self, request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     return super(PontoTuristicoViewSet, self).create(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(self, request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(self, request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     return super(PontoTuristicoViewSet, self).update(self, request, *args, **kwargs)

    # def partial_update(self, request, *args, **kwargs):
    #     return super(PontoTuristicoViewSet, self).partial_update(self, request, *args, **kwargs)

    @action(methods=['post', 'get'], detail=True)
    def denuciar(self, request, pk=None):
        return Response({'denuciar': pk})

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=pk)
        ponto.atracoes.set(atracoes)
        ponto.save()

        return HttpResponse('OK')
