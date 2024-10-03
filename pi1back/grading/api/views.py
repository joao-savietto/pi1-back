from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from pi1back.grading.models import Grading, Subject
from pi1back.grading.api.serializers import GradingSerializer, SubjectSerializer
from pi1back.grading.api.filters import GradingFilter
from pi1back.shared.permissions import IsSuperUserOrReadOnly, IsProfessorOrReadOnly
from django.contrib.auth import get_user_model
from pi1back.classrooms.models import Classroom

User = get_user_model()

@extend_schema_view(
    list=extend_schema(description='Lista todas as notas', summary='Obter lista de notas'),
    retrieve=extend_schema(description='Recuperar uma nota por ID', summary='Obter uma nota específica'),
    create=extend_schema(description='Criar uma nota', summary='Criar uma nova nota'),
    update=extend_schema(description='Atualizar uma nota', summary='Atualizar detalhes de uma nota existente'),
    partial_update=extend_schema(description='Atualizar parcialmente uma nota', summary='Atualizar alguns campos de uma nota existente'),
    destroy=extend_schema(description='Excluir uma nota', summary='Excluir uma nota existente'),
)
class GradingViewSet(viewsets.ModelViewSet):
    queryset = Grading.objects.all()
    serializer_class = GradingSerializer
    permission_classes = [IsSuperUserOrReadOnly | IsProfessorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = GradingFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Grading.objects.all()
        else:
            # Get classrooms the user is a member of
            classrooms = Classroom.objects.filter(members=user)
            # Get students in those classrooms
            students = User.objects.filter(classrooms__in=classrooms)
            # Filter gradings by those students
            return Grading.objects.filter(user__in=students)

@extend_schema_view(
    list=extend_schema(description='Lista todas as disciplinas', summary='Obter lista de disciplinas'),
    retrieve=extend_schema(description='Recuperar uma disciplina por ID', summary='Obter uma disciplina específica'),
    create=extend_schema(description='Criar uma disciplina', summary='Criar uma nova disciplina'),
    update=extend_schema(description='Atualizar uma disciplina', summary='Atualizar detalhes de uma disciplina existente'),
    partial_update=extend_schema(description='Atualizar parcialmente uma disciplina', summary='Atualizar alguns campos de uma disciplina existente'),
    destroy=extend_schema(description='Excluir uma disciplina', summary='Excluir uma disciplina existente'),
)
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsSuperUserOrReadOnly]
