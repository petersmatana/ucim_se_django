from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm


class User(models.Model):
    nazev = models.CharField(max_length=100)
    email = models.EmailField()
    cislo = models.IntegerField()


class UserForm(ModelForm):
    """tady si pretizim formular aby mel jiny chovani
    """
    class Meta:
        model = User
        fields = ['nazev', 'email']
        labels = {
            'nazev': 'muj custom nazev',
            'email': 'elektronicka posta',
        },
