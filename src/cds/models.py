from django.db import models

# Create your models here.

class Quiz(models.Model):
    noquiz = models.CharField(max_length=50)
    evaluation = models.BooleanField()
    intitulequiz = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'quiz'
        unique_together = (('noquiz', 'evaluation'),)