from __future__ import unicode_literals

from django.db import models


class NejakaTabulka(models.Model):
    nazev = models.CharField(max_length=100)
    email = models.EmailField()
    cislo = models.IntegerField()
