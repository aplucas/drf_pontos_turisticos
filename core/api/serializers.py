from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    # comentarios = ComentarioSerializer(many=True, read_only=True)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer()
    decricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'atracoes', 'foto', 'comentarios', 'avaliacoes', 'endereco',
                  'decricao_completa']
        read_only_fields = ['comentarios', 'avaliacoes', ]

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
            ponto.save()

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.save()

        return ponto

    def get_decricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
