# Generated by Django 4.1.2 on 2022-11-14 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('auto_id_quiz', models.AutoField(primary_key=True, serialize=False)),
                ('noquiz', models.CharField(max_length=50)),
                ('evaluation', models.BooleanField()),
                ('intitulequiz', models.CharField(max_length=50)),
                ('actif', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'quiz',
                'unique_together': {('noquiz', 'evaluation')},
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('auto_id_question', models.AutoField(primary_key=True, serialize=False)),
                ('noquestion', models.CharField(max_length=50)),
                ('titrequestion', models.CharField(max_length=200)),
                ('intitulequestion', models.CharField(max_length=200)),
                ('dureequestion', models.TimeField()),
                ('coefquestion', models.IntegerField()),
                ('feedbackquestion', models.CharField(max_length=200)),
                ('bonnereponsequestion', models.IntegerField()),
                ('auto_id_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cds.quiz')),
            ],
            options={
                'db_table': 'questions',
                'unique_together': {('auto_id_quiz', 'noquestion')},
            },
        ),
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
