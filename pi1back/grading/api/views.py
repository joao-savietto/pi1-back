from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from pi1back.grading.models import Grading
from pi1back.grading.api.serializers import GradingSerializer
from pi1back.grading.api.filters import GradingFilter
from pi1back.shared.permissions import IsSuperUserOrReadOnly, IsProfessorOrReadOnly
from django.contrib.auth import get_user_model
from pi1back.classrooms.models import Classroom

User = get_user_model()

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
