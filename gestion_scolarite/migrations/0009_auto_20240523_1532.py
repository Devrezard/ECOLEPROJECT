# Generated by Django 3.1.14 on 2024-05-23 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_scolarite', '0008_eleve_matricule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesinscription',
            name='inscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_scolarite.inscription', unique=True),
        ),
    ]
