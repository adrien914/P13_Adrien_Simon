from django.contrib import admin
from organigramme.models import *

class AdminFiche(admin.ModelAdmin):
    list_display = ["nom" , "email", "pole", "groupe", "fonction", "grade", "etat"]

class AdminFonction(admin.ModelAdmin):
    list_display = ["nom"]

admin.site.register(Fiche, AdminFiche)
admin.site.register(Pole)
admin.site.register(Fonction, AdminFonction)
admin.site.register(Grade)
admin.site.register(Groupe)
# Register your models here.
