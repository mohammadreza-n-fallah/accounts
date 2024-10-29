from django.db import models
from members.models import Member
# Create your models here.



class Account(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    # person=models.ForeignKey(Member,on_delete=models.CASCADE,blank=True)
