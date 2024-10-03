from rest_framework import serializers
from pi1back.grading.models import Grading

class GradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grading
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Calculate the final grade based on the business logic
        final_grade = instance.first_exam + instance.second_exam + instance.third_exam + instance.practice_exam
        
        # Calculate the progress as a percentage
        passing_grade = 5.0  # Assuming the passing grade is 5
        progress = (final_grade / (4 * passing_grade)) * 100  # 4 exams in total
        
        # Add the progress field to the representation
        representation['progress'] = round(progress, 2)  # Round to 2 decimal places
        
        return representation
