from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    codeRole = models.CharField(primary_key=True, max_length=50)
    nomRole = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'role'

class Metier(models.Model):
    codeMetier = models.CharField(primary_key=True, max_length=50)
    nomMetier = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'metier'

class Secteur(models.Model):
    codeSecteur = models.CharField(primary_key=True, max_length=50)
    nomSecteur = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'secteur'

class Utilisateur(AbstractUser):
    matricule = models.CharField(max_length=50, null=False, default="AAAA")
    codeSecteur = models.ForeignKey(Secteur, models.DO_NOTHING, db_column='codeSecteur', null=False, default="MKT")
    codeMetier = models.ForeignKey(Metier, models.DO_NOTHING, db_column='codeMetier', null=False, default="resp_rh")
    codeRole = models.ForeignKey(Role, models.DO_NOTHING, db_column='codeRole', null=False, default="admin")
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["matricule"], name="unique matricule")
        ]
