from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from collab.models import test, Participer, Metier

def index(request):
    metierTest = Metier(codemetier = 'PLB', nommetier = 'Plombier')
    metierTest.save()
    return HttpResponse(Metier.objects.all())