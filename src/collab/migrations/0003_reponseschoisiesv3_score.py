# Generated by Django 4.1.2 on 2022-11-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0002_reponseschoisiesv3_idcollab'),
    ]

    operations = [
        migrations.AddField(
            model_name='reponseschoisiesv3',
            name='score',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]