from django.db import models

from djangotoolbox.fields import ListField, EmbeddedModelField
# Create your models here.

class Brand(models.Model):
    marca = models.CharField(max_length=90)
    modele = ListField(EmbeddedModelField('Modele'))

class Model(models.Model):
    brand = models.ForeignKeyField(Brand, on_delete=models.CASCADE)          
    tip = models.CharField(max_length=90)
    denumire = models.CharField(max_length=90)
    categorie = models.CharField(max_length=90)
    judet_bucati = models.ManyToManyField(Region)

class Region(models.Model):
    judet = models.CharField(max_length=30)
    bucati = models.IntegerField()
    