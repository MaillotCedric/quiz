# Generated by Django 4.1.2 on 2022-11-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReponsesChoisies',
            fields=[
                ('auto_id_reponse_choisie', models.AutoField(primary_key=True, serialize=False)),
                ('noquestion', models.IntegerField()),
                ('propRep1', models.BooleanField(default=False)),
                ('propRep2', models.BooleanField(default=False)),
                ('propRep3', models.BooleanField(default=False)),
                ('propRep4', models.BooleanField(default=False)),
            ],
        ),
    ]