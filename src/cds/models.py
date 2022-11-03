from django.db import models

# Create your models here.

class Quiz(models.Model):
    auto_id_quiz = models.AutoField(primary_key=True)
    noquiz = models.CharField(max_length=50)
    evaluation = models.BooleanField()
    intitulequiz = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'quiz'
        unique_together = (('noquiz', 'evaluation','auto_id_quiz'),) #Au id quiz peut etre enlevé

class Questions(models.Model):
    auto_id_question = models.AutoField(primary_key=True)
    auto_id_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    noquestion = models.CharField(max_length=50)
    titrequestion = models.CharField(max_length=50, blank=True, null=True)
    intitulequestion = models.CharField(max_length=50, blank=True, null=True)
    dureequestion = models.TimeField(blank=True, null=True)
    coefquestion = models.IntegerField(blank=True, null=True)
    feedbackquestion = models.CharField(max_length=50, blank=True, null=True)
    bonnereponsequestion = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'questions'
        unique_together = (('noquestion','auto_id_question'),)