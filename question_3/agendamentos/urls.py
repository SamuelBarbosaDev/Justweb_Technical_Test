from django.urls import path
from agendamentos.views import (
    cancelar_e_editar,
    ListarAgendamentos,
    CadastrarAgendamento,
    AgendamentoEspecifico,
)

urlpatterns = [
    path('cadastrar_agendamento/', CadastrarAgendamento.as_view()),
    path('cancelar_e_editar_agendamento/<int:pk>/', cancelar_e_editar),
    path('listar_agendamentos/', ListarAgendamentos.as_view()),
    path('agendamento/', AgendamentoEspecifico.as_view())
]
