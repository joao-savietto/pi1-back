from rest_framework import viewsets
from ..models import Grading
from .serializers import GradingSerializer
from pi1back.shared.permissions import IsSuperUserOrReadOnly, IsProfessorOrReadOnly

class GradingViewSet(viewsets.ModelViewSet):
    queryset = Grading.objects.all()
    serializer_class = GradingSerializer
    permission_classes = [IsSuperUserOrReadOnly | IsProfessorOrReadOnly]