from django.contrib import admin
from comptes.models import Role, Metier, Secteur, Utilisateur

# Register your models here.

admin.site.register(Role)
admin.site.register(Metier)
admin.site.register(Secteur)
admin.site.register(Utilisateur)
