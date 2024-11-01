from django.shortcuts import render,redirect
from .forms import *
from django.views import View
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages


class PanelView(View):
    def get(self, request):
        return render(request,"panel.html")
class RegisterLoginView(View):
    def get(self,request):

        form=RegisterLoginForm()
        return render(request,"register_login.html",{'form':form})

    def post(self,request):
        if request.method == "POST":
            username=request.POST['username']
            password=request.POST['password']
            if Member.objects.filter(username=username) and Member.objects.filter(password=password):
                messages.success(request,"success")
                return redirect("panel")
            else:

                form = RegisterLoginForm(request.POST)
                # if form.is_valid():
                member = form.save(commit=False)
                member.save()
                messages.success(request, f'Your account has been created ! You are now able to log in')

                return redirect("panel")
        else:
            form = RegisterLoginForm()
            return render(request,"register_login.html",{'form':form})


    
