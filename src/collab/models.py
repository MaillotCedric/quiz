from django.db import models

# Create your models here.

class Test(models.Model):
    nom = models.CharField(max_length=30)
    date_vu = models.DateField(blank=True)
    localisation = models.CharField(max_length=30)

class ReponsesChoisies(models.Model):
    auto_id_reponse_choisie = models.AutoField(primary_key=True)
    noquestion = models.IntegerField()
    propRep1 = models.BooleanField(default=False)
    propRep2 = models.BooleanField(default=False)
    propRep3 = models.BooleanField(default=False)
    propRep4 = models.BooleanField(default=False)
    propRep5 = models.BooleanField(default=False)

    class Meta:
        db_table='reponseschoisies'

class ReponsesChoisiesv2(models.Model):
    auto_id_reponse_choisie2 = models.AutoField(primary_key=True)
    noquestion = models.IntegerField()
    noreponsechoisie = models.IntegerField()

    class Meta:
        db_table='reponseschoisiesv2'
