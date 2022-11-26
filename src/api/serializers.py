from rest_framework import serializers
from comptes.models import Utilisateur, Role
from django.contrib.auth.hashers import make_password

class UtilisateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Utilisateur
        fields = "__all__"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        
        return super(UtilisateurSerializer, self).create(validated_data)

class SecteursSerializer(serializers.Serializer):
    dcount = serializers.IntegerField()
    codeSecteur = serializers.CharField()

    class Meta:
        model = Utilisateur
        fields = ["codeSecteur", "dcount"]
