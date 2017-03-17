from django import forms


class NameForm(forms.Form):
    """tady mam form jak jsem zvykly
    """
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class UserForm(forms.Form):
    nazev = forms.CharField()
    email = forms.EmailField()
    cislo = forms.IntegerField()
