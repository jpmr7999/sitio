# Generated by Django 5.0.6 on 2024-06-26 03:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cliente'),
        ),
    ]
