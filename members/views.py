from django.shortcuts import render
from .forms import *
from django.views import View
from django.http import HttpResponse
# Create your views here.


class RegisterLoginView(View):
    def get(self,request):
        form=RegisterLoginForm()
        return render(request,"register_login.html",{"form":form}) 
    



    
