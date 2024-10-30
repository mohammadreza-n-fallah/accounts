from django.db import models

# Create your models here.



class Member(models.Model):
    username=models.CharField(max_length=200)
    # last_name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200)