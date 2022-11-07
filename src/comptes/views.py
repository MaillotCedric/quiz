from django.shortcuts import render
# from comptes.models import Role
# from comptes.models import Metier
# from comptes.models import Secteur
# from comptes.models import Utilisateur
# from django.contrib.auth.hashers import make_password

def index(request):
    # Role.objects.create(codeRole="admin", nomRole="administrateur")
    # Role.objects.create(codeRole="chef", nomRole="chef de secteur")
    # Role.objects.create(codeRole="collab", nomRole="collaborateur")
    # ---------------------------------------------------------------
    # Metier.objects.create(codeMetier="resp_rh", nomMetier="responsable ressources humaines")
    # Metier.objects.create(codeMetier="dev_web", nomMetier="développeur web")
    # ---------------------------------------------------------------
    # Secteur.objects.create(codeSecteur="MKT", nomSecteur="marketing")
    # Secteur.objects.create(codeSecteur="RD", nomSecteur="recherche et développement")
    # Secteur.objects.create(codeSecteur="RH", nomSecteur="ressources humaines")
    # --------------------------- Création super user ---------------
    # mot_de_passe = make_password("admin")
    # cs = Secteur.objects.get(pk="MKT")
    # cm = Metier.objects.get(pk="resp_rh")
    # cr = Role.objects.get(pk="admin")
    # Utilisateur.objects.create(username="admin", password=mot_de_passe, email="admin@example.com", is_superuser=True, is_staff=True, matricule="AAAA", codeSecteur=cs, codeMetier=cm, codeRole=cr)
    # --------------------------- Création chef secteur RD ----------
    # mot_de_passe = make_password("azerty")
    # cs = Secteur.objects.get(pk="RD")
    # cm = Metier.objects.get(pk="dev_web")
    # cr = Role.objects.get(pk="chef")
    # Utilisateur.objects.create(username="jean", password=mot_de_passe, email="jean@example.com", is_superuser=True, is_staff=True, matricule="AAAB", codeSecteur=cs, codeMetier=cm, codeRole=cr)
    return render(request, "login.html", {})
