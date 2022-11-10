from django.shortcuts import render, redirect
from django.http import HttpResponse
from cds.models import Quiz, Questions
from django.template import loader
from comptes.models import Utilisateur, Secteur
import csv

#-------------------------------------

import xml.etree.ElementTree as etree
import os

# Create your views here.

def get_secteur(elements, secteur):
    code_secteur = elements[0]
    nom_secteur = elements[1]
    secteur["details"] = {}
    secteur["details"]["code_secteur"] = code_secteur
    secteur["details"]["nom_secteur"] = nom_secteur

def get_infos_chef_secteur(elements, secteur):
    matricule_chef_secteur = elements[2]
    nom_chef_secteur = elements[3]
    prenom_chef_secteur = elements[4]
    secteur["chef"] = {}
    secteur["chef"]["matricule"] = matricule_chef_secteur
    secteur["chef"]["nom"] = nom_chef_secteur
    secteur["chef"]["prenom"] = prenom_chef_secteur

def get_infos_collaborateur(elements, secteur):
    matricule_collaborateur = elements[5]
    nom_collaborateur = elements[6]
    prenom_collaborateur = elements[7]
    secteur["collaborateurs"][matricule_collaborateur] = {}
    secteur["collaborateurs"][matricule_collaborateur]["matricule"] = matricule_collaborateur
    secteur["collaborateurs"][matricule_collaborateur]["nom"] = nom_collaborateur
    secteur["collaborateurs"][matricule_collaborateur]["prenom"] = prenom_collaborateur

def index(request, id_chef):
    if request.method == "POST":
        nom_fichier = request.POST["nom_fichier"]
        secteur = {}

        with open("W:/DevIA.E07/FT1B/quiz/secteurs/" + nom_fichier, 'r', newline='') as f:
            reader = csv.reader(f)
            secteur["collaborateurs"] = {}
            for index, row in enumerate(reader):
                elements = row[0].split(";")
                if index == 1:
                    get_secteur(elements, secteur)
                    get_infos_chef_secteur(elements, secteur)
                    get_infos_collaborateur(elements, secteur)
                elif index > 1:
                    get_infos_collaborateur(elements, secteur)
        try: # on vérifie si le secteur existe en base de données
            Secteur.objects.get(pk=secteur["details"]["code_secteur"])
        except: # on crée le secteur en BDD
            Secteur.objects.create(codeSecteur=secteur["details"]["code_secteur"], nomSecteur=secteur["details"]["nom_secteur"])

    if request.user.is_authenticated: # l'utilisateur est bien connecté
        try: # on vérifie que l'id passé dans l'URL existe
            chef = Utilisateur.objects.get(pk=id_chef)
        except: # l'id passé n'existe pas
            return redirect("index_home_cds", id_chef = request.user.id)
        codeSecteur = chef.codeSecteur
        collaborateurs = Utilisateur.objects.filter(codeSecteur=codeSecteur).exclude(codeRole="chef") # collaborateurs du secteur
        if chef.codeRole.pk == "chef": # l'utilisateur est bien un chef
            if request.user.id == int(id_chef): # on empêche un chef de secteur d'aller sur une autre page de chef de secteur
                return render(request, "cds/homeCDS.html", {
                    "chef": chef,
                    "collaborateurs": collaborateurs
                })
            else:
                return redirect("index_home_cds", id_chef = request.user.id) # le chef de secteur est redirigé vers sa page d'acceuil dédiée
        else: # ce n'est pas un chef, c'est donc un collaborateur
            return redirect("home_collab", id_collaborateur = request.user.id) # on renvoie le chef sur sa page d'accueil
    else:
        return redirect("login")

def importQuiz(request):

    doc = etree.parse('../questionnaires/questionnaires_32/32.quv') # À rendre dynamique
    root = doc.getroot()

    try:
        #Créer le quiz 32 dans la table quiz => à rendre dynamique plus tard
        quiz32 = Quiz(noquiz = '32', evaluation=True, intitulequiz='Questionnaire 32') #Attention au auto_id_quiz=1 => statique
        quiz32.save()
    except:
        erreur = 1+1 #Faut bien mettre qq chose...

    #il faut recup la pk en ayant comme condition les contrainte unique!!!!!!!
    pkRecherchee = Quiz.objects.filter(noquiz='32',evaluation=True).values('auto_id_quiz')

    quest32 = {} # À rendre dynamique...
    #Soit envoyer vers BDD plus tard dans le code avec une autre boucle
    #Soit intégrer directement dans les boucle ci-dessous

    i = 0
    #Boucle par balise <question>, récupère ses attributs--------------------------------
    for qst in root:
        i += 1
        #Numero bonne rep
        quest32['bonneRepQ'+str(i)] = qst.get('bonne')
        #Duree #Faire alternative si duree ou pas du style : if(qst.get('duree')) ??
        quest32['dureeQ'+str(i)] = qst.get('duree')
        #Coeff
        quest32['coeffQ'+str(i)] = qst.get('coeff')
        #Image à ajouter ?
        #Insertion dans BDD
        
        try:
            enregistrementBDDQuestion = Questions(auto_id_quiz_id=pkRecherchee,noquestion=i, dureequestion=quest32['dureeQ'+str(i)],coefquestion=quest32['coeffQ'+str(i)], bonnereponsequestion=quest32['bonneRepQ'+str(i)])
            enregistrementBDDQuestion.save()
        except:
            erreur2 = 1+1
        
    #Récupère titre,intitulé et feedback----------------------------------------------
    i2 = 0
    for elt in root.findall("question"):
        i2+=1
        #titre
        quest32['titreQ'+str(i2)] = elt.find('titre').text
        #intitule
        quest32['intituleQ'+str(i2)] = elt.find('intitule').text
        #feedback
        quest32['feedbackQ'+str(i2)] = elt.find('feedback').text

    #Récupère les propositions de reponses-----------------------------------------------
    iQuestion = 0
    for listeReponse in root.findall('.//listerep'):
        iQuestion +=1
        iReponse = 1
        for propRep in listeReponse:
            #print(propRep.text,"reponse=>",iReponse,"question",iQuestion)
            quest32['propRep'+str(iReponse)+'Q'+str(iQuestion)] = propRep.text
            iReponse +=1

    #return redirect('../cds') 
    return HttpResponse(Quiz(auto_id_quiz=1))