from django.forms import ModelForm
from . import models
from .models import Test, ReponsesChoisies, ReponsesChoisiesv2 # changer par=> from cds.models import <nvlTable> ? NON
from django import forms

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ('nom','date_vu','localisation',)

class QuizForm(ModelForm):
    class Meta:
        model = ReponsesChoisies
        fields = ('noquestion','propRep1','propRep2','propRep3','propRep4','propRep5',)

class QuizFormv2(ModelForm):
    class Meta:
        model = ReponsesChoisiesv2
        fields = ('noquestion','noreponsechoisie',)