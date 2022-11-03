from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from collab.models import test, Participer, Metier, Questions

def index(request):
    metierTest = Metier(codemetier = 'JPRO', nommetier = "Joueur Pro")
    metierTest.save()
    return HttpResponse(Metier.objects.all())