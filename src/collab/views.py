from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from comptes.models import Utilisateur

# Create your views here.
from cds.models import Questions, PropositionsReponses, Quiz
from django.template import loader
from collab.models import ReponsesChoisiesv2, ReponsesChoisiesv3

import xml.etree.ElementTree as etree
import os

from .forms import TestForm,QuizForm,QuizFormv2, QuizFormv3

from comptes.models import Utilisateur

def index(request, id_collaborateur):
    #metierTest = Metier(codemetier = 'JPRO', nommetier = "Joueur Pro")
    #metierTest.save()
    # return HttpResponse("Metier.objects.all()")
    if request.user.is_authenticated: # l'utilisateur est bien connecté
        try: # on vérifie que l'id passé dans l'URL existe
            collaborateur = Utilisateur.objects.get(pk=id_collaborateur)
        except: # l'id passé n'existe pas
            return redirect("home_collab", id_collaborateur = request.user.id)
        if collaborateur.codeRole.pk == "collab": # l'utilisateur est bien un collaborateur
            if request.user.id == int(id_collaborateur): # on empêche un collaborateur d'aller sur une autre page de collaborateur
                return render(request, "homeCollab.html", {
                    "collaborateur": collaborateur,
                    "id_collaborateur" : id_collaborateur
                })
            else:
                return redirect("home_collab", id_collaborateur = request.user.id) # le collaborateur est redirigé vers sa page d'acceuil dédiée
        else: # ce n'est pas un collaborateur, c'est donc un chef
            return redirect("index_home_cds", id_chef = request.user.id) # on renvoie le collaborateur sur sa page d'accueil
    else:
        return redirect("login")

def quiz(request, id_collaborateur):
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

def testquiz(request, id_collaborateur):
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
        form = QuizFormv3(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('resultatquiz')
    else:
        form = QuizFormv3
        if 'submitted' in request.GET:
            submitted = True
    
    reponse = ReponsesChoisiesv3.objects.values_list('noquiz')
    # reponse = str(reponse)
    questionbdd = Questions.objects.values()
    codeSecteur = id_collaborateur
    collaborateurs = Utilisateur.objects.get(id=codeSecteur) # collaborateurs du secteur
    context={
        'questions' : questions,
        'form' : form,
        'reponse' : reponse,
        'questionbdd' : questionbdd,
        'collaborateurs' : collaborateurs

    }
    
    return render(request, "collabMain.html", context=context)

def resultatquiz(request, id_collaborateur): # À ajouter => collones id collaborateur dans reponses choisiesv3
    #Recup des reponses et bonnes reponses
    calculScore = {}
    score=0
        #Recup de la bonne rep
    i=0
    for elt in Questions.objects.all(): #Autre solution dans cette boucle => calculScore["bonneRepQ"+str(i)] = elt.bonnereponsequestion
        i+=1
        calculScore["bonneRepQ"+str(i)] = Questions.objects.get(noquestion = i).bonnereponsequestion
    
        #Recup reponses choisies
    i2=1
    while i2 == 1:
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep1
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep2
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep3
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep4
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep5
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep6
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep7
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep8
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep9
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep10
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep11
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep12
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep13
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep14
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep15
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep16
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep17
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep18
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep19
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep20
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep21
        i2+=1
        calculScore["repChoisieQ"+str(i2)] = ReponsesChoisiesv3.objects.get(noquiz = 32).norep22

    #Calcul du score
        #Recup coeff
    i3=0
    for elt in Questions.objects.all():
        i3+=1
        calculScore['coeffQ'+str(i3)] = Questions.objects.get(noquestion = i3).coefquestion
        
        #Calculer les points, comparer les bonnes rep et les repChoisies    
    i4 = 0
    for elt in Questions.objects.all():
        i4+=1
        if calculScore["bonneRepQ"+str(i4)] == calculScore["repChoisieQ"+str(i4)]:
            score += calculScore['coeffQ'+str(i4)]

        #Score final
            #Score max possible
    scoreMax=0
    i5 = 0
    for elt in Questions.objects.all():
        i5 += 1
        point = calculScore['coeffQ'+str(i5)]
        scoreMax += point
            #Calcul final sur 100
    scoreFinal = score * 100 / scoreMax
    
    #Affichage du score

    context={

        'resultat' : calculScore,
        'score' : score,
        'scoremax' : scoreMax,
        'scorefinal' : scoreFinal,
        'id_collaborateur' : id_collaborateur

    }
    return render(request, 'resultat.html', context=context)