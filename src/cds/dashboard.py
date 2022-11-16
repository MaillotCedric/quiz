import numpy as np
from comptes.models import Utilisateur, Secteur

tableau_de_bord = tableau_de_bord = np.empty((2,3,3), dtype=object)

def init_tableau_de_bord():
    tableau_de_bord[0,0,0] = "nom du fichier"
    tableau_de_bord[0,1,0] = "secteur"
    tableau_de_bord[0,2,0] = "chef"
    tableau_de_bord[0,1,1] = "existe"
    tableau_de_bord[0,1,2] = "import unique"
    tableau_de_bord[0,2,1] = "existe"
    tableau_de_bord[0,2,2] = "identique"

def secteur_existe(secteur):
    code_secteur = secteur["details"]["code_secteur"]

    return Secteur.objects.filter(pk=code_secteur).exists()

def secteur_importe_unique(secteur):
    return secteur["nb_secteurs"] == 1

def chef_secteur_existe(secteur):
    code_secteur = secteur["details"]["code_secteur"]
    code_role = "chef"

    return Utilisateur.objects.filter(codeSecteur_id=code_secteur, codeRole_id=code_role).exists()

def chef_secteur_identique(secteur):
    code_secteur = secteur["details"]["code_secteur"]
    code_role = "chef"
    chef_secteur_existant = Utilisateur.objects.get(codeSecteur_id=code_secteur, codeRole_id=code_role)
    chef_secteur_csv = secteur["chef"]

    return chef_secteur_existant.matricule == chef_secteur_csv["matricule"]

def update_tableau_de_bord(nom_fichier, secteur):
    tableau_de_bord[1,0,0] = nom_fichier
    tableau_de_bord[1,1,0] = secteur["details"]["code_secteur"]
    tableau_de_bord[1,2,0] = secteur["chef"]["matricule"]

    if secteur_existe(secteur):
        tableau_de_bord[1,1,1] = True
    else:
        tableau_de_bord[1,1,1] = False

    if secteur_importe_unique(secteur):
        tableau_de_bord[1,1,2] = True
    else:
        tableau_de_bord[1,1,2] = False

    if chef_secteur_existe(secteur):
        tableau_de_bord[1,2,1] = True
        if chef_secteur_identique(secteur):
            tableau_de_bord[1,2,2] = True
        else:
            tableau_de_bord[1,2,2] = False
    else:
        tableau_de_bord[1,2,1] = False
