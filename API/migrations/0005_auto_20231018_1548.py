# Generated by Django 3.2.21 on 2023-10-18 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20231017_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='tipo_de_ouvidoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.ouvidoria'),
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='tipo_de_plataforma',
        ),
        migrations.AddField(
            model_name='feedback',
            name='tipo_de_plataforma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks_plataforma', to='API.plataforma'),
        ),
    ]
