# Generated by Django 3.2.21 on 2023-09-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20230920_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouvidoria',
            name='inativo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='inativo',
            field=models.BooleanField(default=False),
        ),
    ]
