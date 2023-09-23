from typing import Iterable
from agendamentos.models import Agendamentos
from datetime import (
    date,
    datetime,
    timedelta,
    timezone
)


def get_horario_disponiveis(data: date) -> Iterable[datetime]:
    """
    Retorna uma lista com objetos do tipo datetime cujas datas são o mesmo dia
    passado (data) e os horários são os horário disponíveis para aquele dia,
    conforme outros agendamentos existem.
    """

    start = datetime(
        year=data.year,
        month=data.month,
        day=data.day,
        hour=8,
        minute=0,
        tzinfo=timezone.utc
    )
    end = datetime(
        year=data.year,
        month=data.month,
        day=data.day,
        hour=18,
        minute=0,
        tzinfo=timezone.utc
    )
    delta = timedelta(minutes=30)
    horario_disponiveis = set()

    while start < end:
        if not Agendamentos.objects.filter(data=start).exists():
            horario_disponiveis.add(start)
        start = start + delta

    return horario_disponiveis
