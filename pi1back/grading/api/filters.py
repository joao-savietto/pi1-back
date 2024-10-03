from django_filters import rest_framework as filters
from pi1back.grading.models import Grading

class GradingFilter(filters.FilterSet):
    class Meta:
        model = Grading
        fields = ['subject', 'user', 'quarter']
