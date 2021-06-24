from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    endereco = EnderecoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'atracoes', 'foto',
                  'comentarios', 'avaliacoes', 'endereco', 'foto']
