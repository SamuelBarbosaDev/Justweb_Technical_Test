from django.urls import path
from agendamentos.views import AgendamentosList, AgendamentoEspecifico

urlpatterns = [
    path('agendamentos/', AgendamentosList.as_view()),
    path('agendamento/<int:pk>/', AgendamentoEspecifico.as_view())
]
