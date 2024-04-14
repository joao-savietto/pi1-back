# Generated by Django 5.0.3 on 2024-04-13 21:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('members', models.ManyToManyField(related_name='classrooms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('viewed_at', models.DateTimeField(blank=True, null=True)),
                ('is_viewed', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default='')),
                ('occurrence_type', models.CharField(choices=[('ATIVIDADE_NAO_ENTREGUE', 'Atividade não entregue'), ('ATRASO_NA_ENTREGA', 'Atraso na entrega'), ('MAU_COMPORTAMENTO', 'Mau comportamento'), ('FALTOU_AULA', 'Faltou aula'), ('CHEGOU_ATRASADO', 'Chegou atrasado'), ('OUTRO', 'Outro')], default='OUTRO', max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occurrences', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occurrences_student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
