# Generated by Django 5.0.6 on 2024-06-30 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_perfil_cliente_remove_cliente_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='region',
            field=models.CharField(choices=[('REGION_AISEN', 'Región Aisén del General Carlos Ibáñez del Campo'), ('REGION_ARICA_PARINACOTA', 'Región de Arica y Parinacota'), ('REGION_TARAPACA', 'Región de Tarapacá'), ('REGION_LOS_LAGOS', 'Región de Los Lagos'), ('REGION_BERNARDO_OHIGGINS', "Región del Libertador General Bernardo O'Higgins"), ('REGION_BIOBIO', 'Región del Biobío'), ('REGION_ARAUCANIA', 'Región de La Araucanía'), ('REGION_ATACAMA', 'Región de Atacama'), ('REGION_LOS_RIOS', 'Región de Los Ríos'), ('REGION_COQUIMBO', 'Región de Coquimbo'), ('REGION_MAGALLANES', 'Región de Magallanes y de la Antártica Chilena'), ('REGION_VALPARAISO', 'Región de Valparaíso'), ('REGION_MAULE', 'Región del Maule'), ('REGION_NUBLE', 'Región de Ñuble'), ('REGION_ANTOFAGASTA', 'Región de Antofagasta'), ('REGION_METROPOLITANA', 'Región Metropolitana de Santiago')], default='REGION_BIOBIO', max_length=100),
        ),
    ]
