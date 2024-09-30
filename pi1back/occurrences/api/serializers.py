from rest_framework import serializers
from typing import TypedDict
from django.contrib.auth import get_user_model
from pi1back.classrooms.api.serializers import (
    TeacherSerializer,
    StudentSerializer
)

User = get_user_model()

from pi1back.occurrences.models import Occurrence
from pi1back.classrooms.models import Classroom

class OccurrenceSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Occurrence
        exclude = ['created_by']

    def to_internal_value(self, data):
        data = super().to_internal_value(data)     
        data['created_by'] = self.context['request'].user
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['students'] = StudentSerializer(instance.student).data
        if data.get('created_by', None):
            data['teachers'] = TeacherSerializer(instance.created_by).data
            del data['created_by']
        return data