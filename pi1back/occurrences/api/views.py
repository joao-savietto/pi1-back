from rest_framework import viewsets
from ..models import Occurrence, Classroom
from ...shared.permissions import IsProfessorOrReadOnly, IsSuperUserOrReadOnly

from .serializers import (
    OccurrenceSerializer,
    ClassroomSerializer
)

class OccurrenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [IsProfessorOrReadOnly]

class ClassroomViewSet(viewsets.ModelViewSet):
    serializer_class = ClassroomSerializer
    permission_classes = [IsSuperUserOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Classroom.objects.all().prefetch_related('members')
        return Classroom.objects.filter(members=user).prefetch_related('members')
