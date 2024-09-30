from rest_framework import viewsets
from ..models import Classroom
from django.contrib.auth import get_user_model
from pi1back.shared.permissions import IsSuperUserOrReadOnly

from .serializers import (
    ClassroomSerializer
)

User = get_user_model()

class ClassroomViewSet(viewsets.ModelViewSet):
    serializer_class = ClassroomSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = Classroom.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Classroom.objects.all().prefetch_related('members')
        return Classroom.objects.filter(members=user).prefetch_related('members')
