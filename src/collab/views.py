from django.shortcuts import render, redirect
from comptes.models import Utilisateur

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
#from collab.models import Questions

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
                    "collaborateur": collaborateur
                })
            else:
                return redirect("home_collab", id_collaborateur = request.user.id) # le collaborateur est redirigé vers sa page d'acceuil dédiée
        else: # ce n'est pas un collaborateur, c'est donc un chef
            return redirect("index_home_cds", id_chef = request.user.id) # on renvoie le collaborateur sur sa page d'accueil
    else:
        return redirect("login")
