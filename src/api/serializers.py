from rest_framework import serializers
from comptes.models import Utilisateur
from django.contrib.auth.hashers import make_password

class UtilisateurSerializer(serializers.ModelSerializer):
    codeRole = serializers.StringRelatedField()
    codeSecteur = serializers.StringRelatedField()

    class Meta:
        model = Utilisateur
        fields = "__all__"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        
        return super(UtilisateurSerializer, self).create(validated_data)
