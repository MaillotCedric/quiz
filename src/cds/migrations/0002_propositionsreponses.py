# Generated by Django 4.1.2 on 2022-11-07 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropositionsReponses',
            fields=[
                ('auto_id_propositions_reponses', models.AutoField(primary_key=True, serialize=False)),
                ('nopropositionrep', models.IntegerField()),
                ('intitulepropositionreponse', models.CharField(max_length=300)),
                ('auto_id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cds.questions')),
            ],
            options={
                'db_table': 'propositionsreponses',
                'unique_together': {('auto_id_question', 'nopropositionrep')},
            },
        ),
    ]
