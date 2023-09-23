from rest_framework import serializers
from agendamentos.models import Agendamentos


class AgendamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = [
            'nome',
            'email',
            'telefone',
            'data',
            'cancelamento',
        ]
