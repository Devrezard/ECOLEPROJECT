# Generated by Django 3.1.14 on 2024-02-26 12:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnneeScolaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_debut', models.DateField()),
                ('annee_fin', models.DateField()),
                ('annee_scolaire', models.SlugField(editable=False, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('Effectif_classe', models.IntegerField(default=0, editable=False)),
                ('annee_scolaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_scolarite.anneescolaire')),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('date_naissance', models.DateField()),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1)),
                ('numero_pere', models.CharField(max_length=10)),
                ('numero_mere', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inscription', models.DateField(default=django.utils.timezone.now)),
                ('annee_scolaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_scolarite.anneescolaire')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_scolarite.classe')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_scolarite.eleve')),
            ],
        ),
        migrations.CreateModel(
            name='Scolarite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_total', models.BigIntegerField()),
                ('inscription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_scolarite.inscription')),
            ],
        ),
        migrations.CreateModel(
            name='Versement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.BigIntegerField()),
                ('date_paiement', models.DateField(default=django.utils.timezone.now)),
                ('scolarite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_scolarite.scolarite')),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_enseignant', models.CharField(max_length=255)),
                ('prenom_enseignant', models.CharField(max_length=255)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1)),
                ('numero_telephone', models.CharField(max_length=10)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_scolarite.classe')),
            ],
        ),
    ]