# Generated by Django 4.1.2 on 2022-11-03 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cds', '0006_rename_auto_id_questions_questions_auto_id_question_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='quiz',
            unique_together={('noquiz', 'evaluation')},
        ),
    ]
