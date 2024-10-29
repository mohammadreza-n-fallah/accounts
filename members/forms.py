from django import forms

from .models import *



class RegisterLoginForm(forms.ModelForm):
    class Meta:
        model=Member
        fields="__all__"
