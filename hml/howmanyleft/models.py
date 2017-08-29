# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Brand(models.Model):
    marca = models.CharField(max_length=90)

class Region(models.Model):
    judet = models.CharField(max_length=30)
    bucati = models.IntegerField()

class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    tip = models.CharField(max_length=90)
    denumire = models.CharField(max_length=90)
    categorie = models.CharField(max_length=90)
    judet_bucati = models.ManyToManyField(Region)
