from comptes.models import Utilisateur, Secteur, Role
from django.contrib.auth.hashers import make_password

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

    chef_secteur = Utilisateur.objects.filter(codeSecteur_id=code_secteur, codeRole_id=code_role)

    if chef_secteur.exists():
        chef_secteur_actuel = chef_secteur.first()

        if chef_secteur_actuel.matricule != matricule: # le chef de secteur actuel n'est pas celui présenté sur le csv
            # le chef de secteur actuel est passé en collaborateur
            chef_secteur_actuel.codeRole = Role.objects.get(pk="collab")
            chef_secteur_actuel.save()

            # on crée l'employé en tant que chef de secteur
            Utilisateur.objects.create(username=username, password=mot_de_passe, matricule=matricule, first_name=prenom, last_name=nom, codeSecteur=Secteur.objects.get(pk=code_secteur), codeRole=Role.objects.get(pk=code_role))
    else:
        # on crée l'employé en tant que chef de secteur
        Utilisateur.objects.create(username=username, password=mot_de_passe, matricule=matricule, first_name=prenom, last_name=nom, codeSecteur=Secteur.objects.get(pk=code_secteur), codeRole=Role.objects.get(pk=code_role))

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

def create_elements_csv(secteur):
    create_secteur(secteur)
    create_chef_secteur(secteur)
    create_collaborateurs(secteur)
