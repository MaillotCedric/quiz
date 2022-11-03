from django.db import models

# Create your models here.

class Quiz(models.Model):
    noquiz = models.CharField(primary_key=True, max_length=50)
    evaluation = models.BooleanField()
    intitulequiz = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz'
        unique_together = (('noquiz', 'evaluation'),)

class Questions(models.Model):
    noquiz = models.OneToOneField('Quiz', models.DO_NOTHING, db_column='noquiz', primary_key=True)
    evaluation = models.BooleanField()
    noquestion = models.CharField(max_length=50)
    titrequestion = models.CharField(max_length=50, blank=True, null=True)
    intitulequestion = models.CharField(max_length=50, blank=True, null=True)
    dureequestion = models.TimeField(blank=True, null=True)
    coefquestion = models.IntegerField(blank=True, null=True)
    feedbackquestion = models.CharField(max_length=50, blank=True, null=True)
    bonnereponsequestion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'
        unique_together = (('noquiz', 'evaluation', 'noquestion'),)

class Responsablerh(models.Model):
    matriculeresponsablerh = models.CharField(primary_key=True, max_length=50)
    nomresponsablerh = models.CharField(max_length=50, blank=True, null=True)
    prenomresponsablerh = models.CharField(max_length=50, blank=True, null=True)
    idconnexionresponsablerh = models.CharField(max_length=50, blank=True, null=True)
    pwdconnexionresponsablerh = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responsablerh'

class Secteurs(models.Model):
    codesecteur = models.CharField(primary_key=True, max_length=50)
    nomsecteur = models.CharField(max_length=50, blank=True, null=True)
    matriculechefsecteur = models.CharField(max_length=50, blank=True, null=True)
    nomchefsecteur = models.CharField(max_length=50, blank=True, null=True)
    prenomchefsecteur = models.CharField(max_length=50, blank=True, null=True)
    idconnexionchefsecteur = models.CharField(max_length=50, blank=True, null=True)
    pwdconnexionchefsecteur = models.CharField(max_length=50, blank=True, null=True)
    matriculeresponsablerh = models.ForeignKey(Responsablerh, models.DO_NOTHING, db_column='matriculeresponsablerh')

    class Meta:
        managed = False
        db_table = 'secteurs'

class Metier(models.Model):
    codemetier = models.CharField(primary_key=True, max_length=50)
    nommetier = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metier'

class Propositionsreponses(models.Model):
    noquiz = models.OneToOneField('Questions', models.DO_NOTHING, db_column='noquiz', primary_key=True)
    evaluation = models.BooleanField()
    noquestion = models.CharField(max_length=50)
    nopropositionrep = models.IntegerField()
    intitulepropositionreponse = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propositionsreponses'
        unique_together = (('noquiz', 'evaluation', 'noquestion', 'nopropositionrep'),)

class Collaborateur(models.Model):
    matriculecollaborateur = models.CharField(primary_key=True, max_length=50)
    nomcollaborateur = models.CharField(max_length=50, blank=True, null=True)
    prenomcollaborateur = models.CharField(max_length=50, blank=True, null=True)
    idconnexioncollaborateur = models.CharField(max_length=50, blank=True, null=True)
    pwdconnexioncollaborateur = models.CharField(max_length=50, blank=True, null=True)
    codemetier = models.ForeignKey('Metier', models.DO_NOTHING, db_column='codemetier')
    codesecteur = models.ForeignKey('Secteurs', models.DO_NOTHING, db_column='codesecteur')

    class Meta:
        managed = False
        db_table = 'collaborateur'

class Historiquequizcomplete(models.Model):
    matriculecollaborateur = models.OneToOneField(Collaborateur, models.DO_NOTHING, db_column='matriculecollaborateur', primary_key=True)
    dateheure = models.DateField()
    score = models.CharField(max_length=50, blank=True, null=True)
    noquiz = models.ForeignKey('Quiz', models.DO_NOTHING, db_column='noquiz')
    evaluation = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'historiquequizcomplete'
        unique_together = (('matriculecollaborateur', 'dateheure'),)

class Reponseschoisiecollaborateur(models.Model):
    matriculecollaborateur = models.OneToOneField(Historiquequizcomplete, models.DO_NOTHING, db_column='matriculecollaborateur', primary_key=True)
    dateheure = models.DateField()
    noquiz = models.ForeignKey(Questions, models.DO_NOTHING, db_column='noquiz')
    evaluation = models.BooleanField()
    noquestion = models.CharField(max_length=50)
    responsechoisie = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reponseschoisiecollaborateur'
        unique_together = (('matriculecollaborateur', 'dateheure', 'noquiz', 'evaluation', 'noquestion'),)

class Attribuer(models.Model):
    noquiz = models.OneToOneField('Quiz', models.DO_NOTHING, db_column='noquiz', primary_key=True)
    evaluation = models.BooleanField()
    codesecteur = models.ForeignKey('Secteurs', models.DO_NOTHING, db_column='codesecteur')
    dejafaitsecteur = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribuer'
        unique_together = (('noquiz', 'evaluation', 'codesecteur'),)

class Participer(models.Model):
    noquiz = models.OneToOneField('Quiz', models.DO_NOTHING, db_column='noquiz', primary_key=True)
    evaluation = models.BooleanField()
    matriculecollaborateur = models.ForeignKey(Collaborateur, models.DO_NOTHING, db_column='matriculecollaborateur')
    dejafaitcollaborateur = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participer'
        unique_together = (('noquiz', 'evaluation', 'matriculecollaborateur'),)

class test(models.Model):
    ceciTest = models.CharField(max_length=50)

