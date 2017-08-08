from django.db import models

from djangotoolbox.fields import ListField, EmbeddedModelField
# Create your models here.

class Car(models.Model):
    marca = models.CharField(max_length=90)
    modele = ListField(EmbeddedModelField('Modele'))

class Modele(models.Model):
    tip = models.CharField(max_length=90)
    denumire = models.CharField(max_length=90)
    categorie = models.CharField(max_length=90)
    judet_bucati = ListField()