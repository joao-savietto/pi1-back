from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'nome', 'email', 'is_professor', 'is_aluno', 'is_responsavel', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'nome', 'email', 'is_professor', 'is_aluno', 'is_responsavel']
