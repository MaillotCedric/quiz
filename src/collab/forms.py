from django.forms import ModelForm
from . import models
from .models import Test # changer par=> from cds.models import <nvlTable>
from django import forms

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ('nom','date_vu','localisation',)