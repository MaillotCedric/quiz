from django.forms import ModelForm
from . import models
from .models import Test, ReponsesChoisies, ReponsesChoisiesv2, ReponsesChoisiesv3 # changer par=> from cds.models import <nvlTable> ? NON
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

class QuizFormv3(ModelForm):
    class Meta:
        model = ReponsesChoisiesv3
        fields = ('noquiz','norep1','norep2','norep3','norep4','norep5','norep6','norep7','norep8','norep9','norep10','norep11','norep12','norep13','norep14','norep15','norep16','norep17','norep18','norep19','norep20','norep21','norep22','idCollab')