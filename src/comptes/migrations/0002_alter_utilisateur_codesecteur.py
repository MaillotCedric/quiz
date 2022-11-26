# Generated by Django 4.1.2 on 2022-11-26 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='codeSecteur',
            field=models.ForeignKey(db_column='codeSecteur', default='MKT', on_delete=django.db.models.deletion.DO_NOTHING, related_name='code_role', to='comptes.secteur'),
        ),
    ]