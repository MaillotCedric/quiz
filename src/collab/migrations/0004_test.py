# Generated by Django 4.1.2 on 2022-11-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceciTest', models.CharField(max_length=50)),
            ],
        ),
    ]
