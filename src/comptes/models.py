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
    pass
