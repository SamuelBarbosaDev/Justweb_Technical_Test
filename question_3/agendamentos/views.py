from rest_framework import generics
from agendamentos.models import Agendamentos
from agendamentos.serializers import AgendamentosSerializer


class AgendamentosList(generics.ListCreateAPIView):
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentosSerializer
