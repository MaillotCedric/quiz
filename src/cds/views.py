from django.shortcuts import render, redirect
from django.http import HttpResponse
from collab.models import Metier
from django.template import loader

# Create your views here.

def index(request):

    return render (request, "cds/homeCDS.html")

def importQuiz(request):

    #return redirect('../cds') 
    return HttpResponse("testBouton")