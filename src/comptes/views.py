from django.shortcuts import render
# from comptes.models import Role

def index(request):
    # Role.objects.create(codeRole="admin", nomRole="administrateur")
    # Role.objects.create(codeRole="chef", nomRole="chef de secteur")
    # Role.objects.create(codeRole="collab", nomRole="collaborateur")
    return render(request, "login.html", {})
