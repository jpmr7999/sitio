# Generated by Django 5.0.6 on 2024-06-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_cliente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='correo',
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
