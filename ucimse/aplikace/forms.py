from django import forms

# vsechny mozne input type
# https://docs.djangoproject.com/en/1.10/ref/forms/fields/


class NameForm(forms.Form):
    # formular = forms.CharField(label='Muj popisek', max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
