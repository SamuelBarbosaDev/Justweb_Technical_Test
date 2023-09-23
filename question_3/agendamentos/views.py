from rest_framework import status
from rest_framework import generics
from django.http import JsonResponse
from rest_framework import permissions
from agendamentos.models import Agendamentos
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from agendamentos.serializers import AgendamentosSerializer
from rest_framework.decorators import (
    api_view,
    permission_classes
)


class CadastrarAgendamento(generics.CreateAPIView):
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentosSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(http_method_names=['PATCH', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def cancelar_e_editar(request, pk):
    obj = get_object_or_404(klass=Agendamentos, id=pk)

    if request.method == 'PATCH':
        serializer = AgendamentosSerializer(
            instance=obj,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return JsonResponse(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'DELETE':
        obj.cancelamento = True
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListarAgendamentos(generics.ListCreateAPIView):
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AgendamentoEspecifico(generics.RetrieveAPIView):
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentosSerializer
    permission_classes = [permissions.IsAuthenticated]
