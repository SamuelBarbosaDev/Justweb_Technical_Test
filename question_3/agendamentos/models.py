from django.db import models


class Agendamentos(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=13)
    data = models.DateTimeField()
    cancelamento = models.BooleanField(default=False)
