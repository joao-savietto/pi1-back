from rest_framework import serializers
from pi1back.grading.models import Grading

class GradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grading
        fields = '__all__'
