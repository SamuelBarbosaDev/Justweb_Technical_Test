from django.utils import timezone
from agendamentos.models import Agendamentos
from rest_framework import serializers, status
from agendamentos.utils import get_horario_disponiveis


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

    def validate_data(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                detail='O agendamento não pode ser feito no passado.',
                code=status.HTTP_400_BAD_REQUEST
            )

        if value not in get_horario_disponiveis(value.date()):
            raise serializers.ValidationError(
                'Esse horário não está disponível.'
            )

        return value
