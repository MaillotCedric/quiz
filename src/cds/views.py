from django.shortcuts import render, redirect
from django.http import HttpResponse
from cds.models import Quiz, Questions
from django.template import loader
from comptes.models import Utilisateur, Secteur, Role
from django.contrib.auth.hashers import make_password
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
    secteur["collaborateurs"].append({
        "matricule": matricule_collaborateur,
        "nom": nom_collaborateur,
        "prenom": prenom_collaborateur
    })

def create_secteur(secteur):
    code_secteur = secteur["details"]["code_secteur"]
    nom_secteur = secteur["details"]["nom_secteur"]

    secteur_a_creer = Secteur.objects.filter(pk=code_secteur)

    if not secteur_a_creer.exists(): # si le secteur n'existe pas en base de données,
        # on le crée
        Secteur.objects.create(codeSecteur=code_secteur, nomSecteur=nom_secteur)

def create_chef_secteur(secteur):
    mot_de_passe = make_password("azerty")
    code_secteur = secteur["details"]["code_secteur"]
    code_role = "chef"
    username = secteur["chef"]["matricule"]
    matricule = secteur["chef"]["matricule"]
    nom = secteur["chef"]["nom"]
    prenom = secteur["chef"]["prenom"]

    employe = Utilisateur.objects.filter(matricule=matricule)

    if employe.exists(): # si l'employé est enregistré en BDD,
        # on le passe en chef de secteur
        employe_a_modifier = employe.first()
        employe_a_modifier.codeRole = Role.objects.get(pk="chef")
        employe_a_modifier.save()
    else:
        # on crée l'employé en tant que chef de secteur
        Utilisateur.objects.create(username=username, password=mot_de_passe, matricule=matricule, first_name=prenom, last_name=nom, codeSecteur=Secteur.objects.get(pk=code_secteur), codeRole=Role.objects.get(pk=code_role))

    # on sélectionne tout les chefs de secteurs
    chefs_secteur = Utilisateur.objects.filter(codeSecteur_id=code_secteur, codeRole_id=code_role)

    if chefs_secteur.count() > 1: # si il existe plusieurs chef de secteur pour ce secteur,
        # on exclut celui présenté comme chef de secteur sur le csv
        chefs_secteur = chefs_secteur.exclude(matricule=matricule)
        # on passe les chefs de secteurs restants en tant que collaborateur
        for chef_secteur in chefs_secteur:
            chef_secteur.codeRole = Role.objects.get(pk="collab")
            chef_secteur.save()

def create_collaborateurs(secteur):
    mot_de_passe = make_password("azerty")
    code_secteur = secteur["details"]["code_secteur"]
    code_role = "collab"
    nouveaux_collaborateurs = secteur["collaborateurs"]

    anciens_collaborateurs = Utilisateur.objects.filter(codeSecteur_id=code_secteur, codeRole_id=code_role)
    if anciens_collaborateurs.exists(): # si il existe des collaborateurs dans le secteur sélectionné
        # on les efface de la base de données
        for ancien_collaborateur in anciens_collaborateurs:
            ancien_collaborateur.delete()
    
    # on crée les collaborateurs présents sur le csv
    for nouveau_collaborateur in nouveaux_collaborateurs:
        username = nouveau_collaborateur["matricule"]
        matricule = nouveau_collaborateur["matricule"]
        prenom = nouveau_collaborateur["prenom"]
        nom = nouveau_collaborateur["nom"]

        Utilisateur.objects.create(username=username, password=mot_de_passe, matricule=matricule, first_name=prenom, last_name=nom, codeSecteur=Secteur.objects.get(pk=code_secteur), codeRole=Role.objects.get(pk=code_role))

def index(request, id_chef):
    if request.method == "POST":
        nom_fichier = request.POST["nom_fichier"]
        secteur = {}

        with open("W:/DevIA.E07/FT1B/quiz/secteurs/" + nom_fichier, 'r', newline='') as f:
            reader = csv.reader(f)
            secteur["collaborateurs"] = []
            for index, row in enumerate(reader):
                elements = row[0].split(";")
                if index == 1:
                    get_secteur(elements, secteur)
                    get_infos_chef_secteur(elements, secteur)
                    get_infos_collaborateur(elements, secteur)
                elif index > 1:
                    get_infos_collaborateur(elements, secteur)
        create_secteur(secteur)
        create_chef_secteur(secteur)
        create_collaborateurs(secteur)

    if request.user.is_authenticated: # l'utilisateur est bien connecté
        try: # on vérifie que l'id passé dans l'URL existe
            chef = Utilisateur.objects.get(pk=id_chef)
        except: # l'id passé n'existe pas
            return redirect("index_home_cds", id_chef = request.user.id)
        codeSecteur = chef.codeSecteur
        collaborateurs = Utilisateur.objects.filter(codeSecteur=codeSecteur).exclude(codeRole="chef").exclude(codeRole="admin") # collaborateurs du secteur
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