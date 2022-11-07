from django.shortcuts import render
# from comptes.models import Role
# from comptes.models import Metier
# from comptes.models import Secteur

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
    return render(request, "login.html", {})
