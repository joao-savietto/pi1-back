from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from ..models import Classroom
from django.contrib.auth import get_user_model
from pi1back.shared.permissions import IsSuperUserOrReadOnly

from .serializers import (
    ClassroomSerializer
)

User = get_user_model()

@extend_schema_view(
    list=extend_schema(description='Lista todas as salas de aula', summary='Obter lista de salas de aula'),
    retrieve=extend_schema(description='Recuperar uma sala de aula por ID', summary='Obter uma sala de aula específica'),
    create=extend_schema(description='Criar uma sala de aula', summary='Criar uma nova sala de aula'),
    update=extend_schema(description='Atualizar uma sala de aula', summary='Atualizar detalhes de uma sala de aula existente'),
    partial_update=extend_schema(description='Atualizar parcialmente uma sala de aula', summary='Atualizar alguns campos de uma sala de aula existente'),
    destroy=extend_schema(description='Excluir uma sala de aula', summary='Excluir uma sala de aula existente'),
)
class ClassroomViewSet(viewsets.ModelViewSet):
    serializer_class = ClassroomSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = Classroom.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Classroom.objects.all().prefetch_related('members')
        return Classroom.objects.filter(members=user).prefetch_related('members')
