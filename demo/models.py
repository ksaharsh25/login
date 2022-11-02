from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.EmailField(max_length=50,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)

class Mobile(models.Model):
    mobile=models.IntegerField(max_length=10,blank=True,null=True) 
    otp=models.IntegerField(max_length=10,blank=True,null=True)    