from rest_framework import serializers
from ...classrooms.models import Classroom
from django.contrib.auth import get_user_model


User = get_user_model()


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'nome']

class StudentSerializer(serializers.ModelSerializer):
    occurrence_count = serializers.SerializerMethodField()

    def get_occurrence_count(self, obj) -> int:
        return obj.student_occurrences.count()

    class Meta:
        model = User
        fields = ['id', 'nome', 'occurrence_count']

class ClassroomSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['teachers'] = TeacherSerializer(instance.members.filter(is_professor=True), many=True).data
        representation['students'] = StudentSerializer(instance.members.filter(is_aluno=True), many=True).data
        return representation