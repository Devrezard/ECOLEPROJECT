# Generated by Django 3.1.14 on 2024-05-27 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_scolarite', '0010_auto_20240523_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesinscription',
            name='inscription',
            field=models.OneToOneField(error_messages={'unique': "Il existe déjà un enregistrement d'articles pour cet élève."}, on_delete=django.db.models.deletion.CASCADE, to='gestion_scolarite.inscription'),
        ),
        migrations.AlterField(
            model_name='classe',
            name='nom',
            field=models.CharField(choices=[('CP1', 'CP1'), ('CP2', 'CP2'), ('CE1', 'CE1'), ('CE2', 'CE2'), ('CM1', 'CM1'), ('CM2', 'CM2')], max_length=255),
        ),
    ]
