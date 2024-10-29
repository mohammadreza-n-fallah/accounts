from django.shortcuts import render
from .forms import *
# Create your views here.


class RegisterLoginView():
    def get():
        form=RegisterLoginForm()
        return ("register_login",{form})