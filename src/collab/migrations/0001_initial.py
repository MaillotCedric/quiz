# Generated by Django 4.1.2 on 2022-11-09 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('date_vu', models.DateField(blank=True)),
                ('localisation', models.CharField(max_length=30)),
            ],
        ),
    ]
