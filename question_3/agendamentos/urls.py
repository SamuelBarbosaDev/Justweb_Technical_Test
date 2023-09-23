from django.urls import path
from agendamentos.views import AgendamentosList

urlpatterns = [
    path('agendamentos/', AgendamentosList.as_view()),
]
