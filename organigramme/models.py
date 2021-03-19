from django.db import models


class Pole(models.Model):
    nom = models.CharField(max_length=255, unique=True, blank=False,)
    group = models.IntegerField()
    classement = models.IntegerField()
    def __str__(self):
        return self.nom


class Fonction(models.Model):
    nom = models.CharField(max_length=255, unique=True, blank=False,)

    def __str__(self):
        return self.nom


class Groupe(models.Model):
    nom = models.CharField(max_length=255, unique=True, blank=False,)
    importance = models.IntegerField(default=999, blank=False)

    def __str__(self):
        return self.nom


class Grade(models.Model):
    nom = models.CharField(max_length=255, unique=True, blank=False,)

    def __str__(self):
        return self.nom


class Fiche(models.Model):
    nom = models.CharField(max_length=255, blank=False,)
    email = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    rang_affichage = models.IntegerField()  # Rang de la personne dans sa fonction
    image = models.CharField(max_length=255, blank=True, null=True)
    etat = models.CharField(max_length=255, choices=[('pub', 'Publié'), ('not_pub', 'Non publié')])  # publié / non publié
    nombre_elements_ligne = models.CharField(max_length=255, choices=[('col-4', '3'), ('col-6', '2'), ('col-12', '1')], default='col-4')
    pole = models.ForeignKey(to=Pole, on_delete=models.CASCADE, blank=True, null=True)
    fonction = models.ForeignKey(to=Fonction, on_delete=models.CASCADE, blank=True, null=True)
    groupe = models.ForeignKey(to=Groupe, on_delete=models.CASCADE, blank=True, null=True)
    grade = models.ForeignKey(to=Grade, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nom
