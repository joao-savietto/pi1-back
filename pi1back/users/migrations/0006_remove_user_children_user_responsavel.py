# Generated by Django 5.0.2 on 2024-05-15 04:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_children'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='children',
        ),
        migrations.AddField(
            model_name='user',
            name='responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
