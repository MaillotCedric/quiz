from rest_framework.response import Response
from rest_framework.decorators import api_view
from comptes.models import Utilisateur
from .serializers import UtilisateurSerializer, SecteursSerializer
from django.db.models import Count

@api_view(["GET"])
def get_users(request):
    utilisateurs = Utilisateur.objects.all()
    serializer = UtilisateurSerializer(utilisateurs, many=True)

    return Response(serializer.data)

@api_view(["POST"])
def add_users(request):
    serializer = UtilisateurSerializer(data=request.data)
    # new_user = {
    #     "username": "toto",
    #     "password": "azerty",
    #     "matricule": "CCCC",
    #     "codeSecteur": "RD",
    #     "codeRole": "collab"
    # }
    # serializer = UtilisateurSerializer(data=new_user)

    if serializer.is_valid(raise_exception=True):
        print("valid !!!")
        serializer.save()

    return Response(serializer.data)

@api_view(["POST"])
def delete_user(request):
    matricule = request.query_params.get("matricule")
    utilisateur = Utilisateur.objects.get(matricule=matricule)
    nom_utilisateur = utilisateur.username
    id_utilisateur = utilisateur.id

    utilisateur.delete()

    return Response({"nom_utilisateur": nom_utilisateur, "id_utilisateur": id_utilisateur})

@api_view(["GET"])
def get_secteurs(request):
    secteurs = Utilisateur.objects.values('codeSecteur').annotate(dcount=Count("codeSecteur"))
    serializer = SecteursSerializer(secteurs, many=True)

    return Response(serializer.data)
