from django import forms
from django.forms import ModelForm,TextInput,EmailField
from .models import *



class RegisterLoginForm(forms.ModelForm):
        class Meta:
            model = Member
            fields = ['username',"email", 'password']
            widgets = {
                'email': forms.TextInput(attrs={
                    'class': "form-control", 
                    'style': 'width: 300px;border-radius: 5px;height:40px;border: 2px solid black',
                    'placeholder': 'email'
                    }),
                'username': forms.TextInput(attrs={
                    'class': "form-control",
                    'style': 'width: 300px;border-radius: 5px;height:40px;border: 2px solid black',
                    'placeholder': 'username'
                    }),
              
                'password': forms.TextInput(attrs={
                    'class': "form-control", 
                    'style': 'width: 300px;border-radius: 5px;height:40px;border: 2px solid black',
                    'placeholder': 'password'
                    })
            }
