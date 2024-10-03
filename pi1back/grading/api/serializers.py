from rest_framework import serializers
from pi1back.grading.models import Grading, Subject

class GradingSerializer(serializers.ModelSerializer):
    subject_id =  serializers.IntegerField(read_only=True)
    final_grade = serializers.FloatField(write_only=True, default=0)

    class Meta:
        model = Grading
        fields = ['id', 'subject', 'user', 'first_exam', 
        'second_exam', 'third_exam', 'practice_exam', 
        'year', 'quarter', 'subject_id', 'final_grade']

    def create(self, validated_data):
        # Calculate the final grade
        final_grade = validated_data['first_exam'] + validated_data['second_exam'] + validated_data['third_exam'] + validated_data['practice_exam']
        validated_data['final_grade'] = final_grade
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Calculate the final grade
        final_grade = validated_data.get('first_exam', instance.first_exam) + validated_data.get('second_exam', instance.second_exam) + validated_data.get('third_exam', instance.third_exam) + validated_data.get('practice_exam', instance.practice_exam)
        instance.final_grade = final_grade
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Calculate the progress as a percentage
        passing_grade = 5.0  # Assuming the passing grade is 5
        progress = (instance.final_grade / (4 * passing_grade)) * 100  # 4 exams in total
        
        # Add the progress field to the representation
        representation['progress'] = round(progress, 2)  # Round to 2 decimal places
        representation["subject_id"] = instance.subject.id
        representation["subject"] = instance.subject.name
        
        return representation

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
