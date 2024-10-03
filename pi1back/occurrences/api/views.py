from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from ..models import Occurrence
from ...shared.permissions import IsProfessorOrReadOnly, IsSuperUserOrReadOnly
from django.contrib.auth import get_user_model

User = get_user_model()

from .serializers import (
    OccurrenceSerializer,
)

from .filters import OccurrenceFilter

@extend_schema_view(
    list=extend_schema(description='Lista todas as ocorrências', summary='Obter lista de ocorrências'),
    retrieve=extend_schema(description='Recuperar uma ocorrência por ID', summary='Obter uma ocorrência específica'),
    create=extend_schema(description='Criar uma ocorrência', summary='Criar uma nova ocorrência'),
    update=extend_schema(description='Atualizar uma ocorrência', summary='Atualizar detalhes de uma ocorrência existente'),
    partial_update=extend_schema(description='Atualizar parcialmente uma ocorrência', summary='Atualizar alguns campos de uma ocorrência existente'),
    destroy=extend_schema(description='Excluir uma ocorrência', summary='Excluir uma ocorrência existente'),
)

class OccurrenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [IsProfessorOrReadOnly]
    filterset_class = OccurrenceFilter

    def get_queryset(self):
        qs = Occurrence.objects.all()
        if self.request.user.is_responsavel:
            children = User.objects.filter(responsavel = self.request.user).all()
            qs = qs.filter(student__in = children).all()
        return qs
