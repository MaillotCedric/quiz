from rest_framework.response import Response
from rest_framework.decorators import api_view
from comptes.models import Utilisateur
from .serializers import UtilisateurSerializer

@api_view(["GET"])
def get_users(request):
    utilisateurs = Utilisateur.objects.all()
    serializer = UtilisateurSerializer(utilisateurs, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def add_users(request):
    # serializer = UtilisateurSerializer(data=request.data)
    new_user = {
        "username": "toto",
        "password": "azerty",
        "matricule": "CCCC",
        "codeSecteur": "RD",
        "codeRole": "collab"
    }
    serializer = UtilisateurSerializer(data=new_user)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
