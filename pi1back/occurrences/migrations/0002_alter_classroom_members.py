# Generated by Django 5.0.3 on 2024-04-13 23:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='classrooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
