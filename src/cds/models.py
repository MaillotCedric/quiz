from django.db import models

# Create your models here.

class Quiz(models.Model):
    noquiz = models.CharField(max_length=50)
    evaluation = models.BooleanField()
    intitulequiz = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'quiz'
        unique_together = (('noquiz', 'evaluation'),)

class Questions(models.Model):
    noquiz = models.OneToOneField('Quiz', models.DO_NOTHING, db_column='noquiz')
    evaluation = models.BooleanField()
    noquestion = models.CharField(max_length=50)
    titrequestion = models.CharField(max_length=50, blank=True, null=True)
    intitulequestion = models.CharField(max_length=50, blank=True, null=True)
    dureequestion = models.TimeField(blank=True, null=True)
    coefquestion = models.IntegerField(blank=True, null=True)
    feedbackquestion = models.CharField(max_length=50, blank=True, null=True)
    bonnereponsequestion = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'questions'
        unique_together = (('noquiz', 'evaluation', 'noquestion'),)