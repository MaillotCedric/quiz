from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from cds.models import Questions, PropositionsReponses, Quiz
from django.template import loader
from collab.models import ReponsesChoisiesv2

import xml.etree.ElementTree as etree
import os

from .forms import TestForm,QuizForm,QuizFormv2

def index(request):

    return render(request, "collabMain.html")

def quiz(request):
    doc = etree.parse('../questionnaires/questionnaires_32/32.quv') # À rendre dynamique
    root = doc.getroot()
    quest32={}
    pkRecherchee = Quiz.objects.filter(noquiz='32',evaluation=True).values('auto_id_quiz')
    #------------------------------------------
    iQuestion = 0
    for listeReponse in root.findall('.//listerep'):
        iQuestion +=1
        iReponse = 1
        for propRep in listeReponse:
            #print(propRep.text,"reponse=>",iReponse,"question",iQuestion)
            quest32['propRep'+str(iReponse)+'Q'+str(iQuestion)] = propRep.text
            #Enregistrement dans BDD
            iReponse +=1
    #------------------------------------------
    i2 = 0
    for elt in root.findall("question"):
        i2+=1
        #titre
        quest32['titreQ'+str(i2)] = elt.find('titre').text
        #intitule
        quest32['intituleQ'+str(i2)] = elt.find('intitule').text
        #feedback
        quest32['feedbackQ'+str(i2)] = elt.find('feedback').text
    questions = quest32
    #results = open("collab/static/quiz.js", "r")
    #test = results.read
    context={
        'questions' : questions,
        #'resultat' : test
    }
    
    return render (request, "collabMain.html", context=context)

def test(request):
    submitted = False
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
    else:
        form = TestForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, "form.html", {'form': form})

def testquiz(request):
    #------------------------------------recup des questions dans XML------------------------------------------
    doc = etree.parse('../questionnaires/questionnaires_32/32.quv') # À rendre dynamique
    root = doc.getroot()
    quest32={}
    pkRecherchee = Quiz.objects.filter(noquiz='32',evaluation=True).values('auto_id_quiz')
    #------------------------------------------
    iQuestion = 0
    for listeReponse in root.findall('.//listerep'):
        iQuestion +=1
        iReponse = 1
        for propRep in listeReponse:
            #print(propRep.text,"reponse=>",iReponse,"question",iQuestion)
            quest32['propRep'+str(iReponse)+'Q'+str(iQuestion)] = propRep.text
            #Enregistrement dans BDD
            iReponse +=1
    #------------------------------------------
    i2 = 0
    for elt in root.findall("question"):
        i2+=1
        #titre
        quest32['titreQ'+str(i2)] = elt.find('titre').text
        #intitule
        quest32['intituleQ'+str(i2)] = elt.find('intitule').text
        #feedback
        quest32['feedbackQ'+str(i2)] = elt.find('feedback').text
    questions = quest32
    #----------------------------------------------------------------------------------------------------------
    submitted = False
    if request.method == "POST":
        form = QuizFormv2(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
    else:
        form = QuizFormv2
        if 'submitted' in request.GET:
            submitted = True
    
    reponse = ReponsesChoisiesv2.objects.values_list('noquestion')
    # reponse = str(reponse)
    context={
        'questions' : questions,
        'form' : form,
        'reponse' : reponse
    }
    
    return render(request, "collabMain.html", context=context)
