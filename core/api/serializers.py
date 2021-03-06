from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from core.models import PontoTuristico, DocIdentificacao
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    # comentarios = ComentarioSerializer(many=True, read_only=True)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer()
    decricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'atracoes', 'foto', 'comentarios', 'avaliacoes', 'endereco',
                  'decricao_completa', 'doc_identificacao', 'aprovado']
        read_only_fields = ['comentarios', 'avaliacoes', ]

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
            # ponto.save()

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']
        end = Endereco.objects.create(**endereco)

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto

    def get_decricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
