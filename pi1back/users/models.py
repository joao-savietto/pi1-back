from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    is_professor = models.BooleanField(default=False)
    is_aluno = models.BooleanField(default=False)
    is_responsavel = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']