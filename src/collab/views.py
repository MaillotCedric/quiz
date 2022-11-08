from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from cds.models import Questions, PropositionsReponses, Quiz
from django.template import loader

def index(request):

    return render(request, "collabMain.html")