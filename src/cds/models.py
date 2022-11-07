from django.db import models

# Create your models here.

class Quiz(models.Model):
    auto_id_quiz = models.AutoField(primary_key=True)
    noquiz = models.CharField(max_length = 50)
    evaluation = models.BooleanField()
    intitulequiz = models.CharField(max_length=50)

    class Meta:
        db_table = 'quiz'
        unique_together = (('noquiz','evaluation'))

class Questions(models.Model):
    auto_id_question = models.AutoField(primary_key=True)
    noquestion = models.CharField(max_length=50)
    titrequestion = models.CharField(max_length=200)
    intitulequestion = models.CharField(max_length=200)
    dureequestion = models.TimeField()
    coefquestion = models.IntegerField()
    feedbackquestion = models.CharField(max_length=200)
    bonnereponsequestion = models.IntegerField()
    auto_id_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        db_table = 'questions'
        unique_together = (('auto_id_quiz','noquestion'))

