from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from comptes.models import Role
# from comptes.models import Metier
# from comptes.models import Secteur
# from comptes.models import Utilisateur
# from django.contrib.auth.hashers import make_password

# def index(request):
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
    # --------------------------- Création collaborateurs RD ---------
    # mot_de_passe = make_password("azerty")
    # cs = Secteur.objects.get(pk="RD")
    # cm = Metier.objects.get(pk="dev_web")
    # cr = Role.objects.get(pk="collab")
    # Utilisateur.objects.create(username="jacques", password=mot_de_passe, email="jacques@example.com", matricule="AAAC", codeSecteur=cs, codeMetier=cm, codeRole=cr)
    # Utilisateur.objects.create(username="marie", password=mot_de_passe, email="marie@example.com", matricule="AAAD", codeSecteur=cs, codeMetier=cm, codeRole=cr)
    # ------------------- test contrainte d'unicité matricule -------
    # mot_de_passe = make_password("azerty")
    # cs = Secteur.objects.get(pk="RD")
    # cm = Metier.objects.get(pk="dev_web")
    # cr = Role.objects.get(pk="collab")
    # Utilisateur.objects.create(username="laurent", password=mot_de_passe, email="laurent@example.com", matricule="AAAC", codeSecteur=cs, codeMetier=cm, codeRole=cr)
    # ------------------- test contrainte d'unicité role(chef)/secteur -------
    # mot_de_passe = make_password("azerty")
    # cs = Secteur.objects.get(pk="RD")
    # cm = Metier.objects.get(pk="dev_web")
    # cr = Role.objects.get(pk="chef")
    # Utilisateur.objects.create(username="paul", password=mot_de_passe, email="paul@example.com", matricule="AAAE", codeSecteur=cs, codeMetier=cm, codeRole=cr)
    # return render(request, "login.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("login success"))
            return render(request, "login.html", {
                "role": user.codeRole.pk
            })
        else:
            messages.success(request, ("login erreur"))
            return render(request, "login.html", {})
    else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("logged out"))
    return redirect("login")
