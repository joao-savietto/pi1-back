from rest_framework import viewsets
from ..models import Grading
from .serializers import GradingSerializer

class GradingViewSet(viewsets.ModelViewSet):
    queryset = Grading.objects.all()
    serializer_class = GradingSerializer
