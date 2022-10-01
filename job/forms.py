from django import forms
from django.utils.datetime_safe import datetime

from .models import apply,job

class applyform(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['name', 'email', 'website', 'cv' , 'cover_letter']

class jobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('slug','owner')