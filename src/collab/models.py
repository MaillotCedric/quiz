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

class ReponsesChoisiesv3(models.Model):
    auto_id_reponse_choisie3 = models.AutoField(primary_key=True)
    noquiz = models.CharField(max_length=50)
    norep1 = models.IntegerField(null=True, blank=True)
    norep2 = models.IntegerField(null=True, blank=True)
    norep3 = models.IntegerField(null=True, blank=True)
    norep4 = models.IntegerField(null=True, blank=True)
    norep5 = models.IntegerField(null=True, blank=True)
    norep6 = models.IntegerField(null=True, blank=True)
    norep7 = models.IntegerField(null=True, blank=True)
    norep8 = models.IntegerField(null=True, blank=True)
    norep9 = models.IntegerField(null=True, blank=True)
    norep10 = models.IntegerField(null=True, blank=True)
    norep11 = models.IntegerField(null=True, blank=True)
    norep12 = models.IntegerField(null=True, blank=True)
    norep13 = models.IntegerField(null=True, blank=True)
    norep14 = models.IntegerField(null=True, blank=True)
    norep15 = models.IntegerField(null=True, blank=True)
    norep16 = models.IntegerField(null=True, blank=True)
    norep17 = models.IntegerField(null=True, blank=True)
    norep18 = models.IntegerField(null=True, blank=True)
    norep19 = models.IntegerField(null=True, blank=True)
    norep20= models.IntegerField(null=True, blank=True)
    norep21 = models.IntegerField(null=True, blank=True)
    norep22 = models.IntegerField(null=True, blank=True)
    idCollab = models.IntegerField(null=True, blank=True)
    score = models.CharField(max_length=50, null=True,blank=True)
    datePassage = models.CharField(max_length=50, null=True,blank=True)

    class Meta:
        db_table='reponseschoisiesv3'

