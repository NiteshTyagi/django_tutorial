from django.db import models

# Create your models here.

from django import forms


class Contactus(forms.Form):

    first_name = forms.CharField(max_length='120')
    last_name = forms.CharField(max_length='120')

    email_address = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)

    image = forms.ImageField()
