# Generated by Django 4.1.2 on 2022-11-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0005_alter_metier_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='metier',
            name='testFredy',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
