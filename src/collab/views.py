from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from cds.models import Questions, PropositionsReponses, Quiz
from django.template import loader

import xml.etree.ElementTree as etree

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
    context={
        'questions' : questions
    }
    return render (request, "collabMain.html", context=context)