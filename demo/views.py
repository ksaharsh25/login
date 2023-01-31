from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,Http404
# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
import random 

class Logingeneric(generics.ListAPIView,generics.CreateAPIView):
    queryset=Login.objects.all()
    serializer_class = DemoSerializer

        

class LoginGeneric(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset=Login.objects.all()
    serializer_class = DemoSerializer
    lookup_field='id'


def http(request):
    if request.method== 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= Login.objects.filter(email=email,password=password)
        print(email)
        print(password)
        if user.exists():
            return HttpResponse("chal gaya")
        else:   
            return HttpResponse("404 error!")
           
    return render(request,"login.html")          

def get_otp():
    otp = ""
    for i in range(4):
        otp += str(random.randint(1,9))
    return otp


def mobile(request):
    if request.method =="POST":
       mobile=request.POST.get('mobile')
       
       try:
        Mob=Mobile.objects.get(mobile=mobile)
        
       

       except:
        Mobile.objects.create(mobile=mobile)
        Mob=Mobile.objects.get(mobile=mobile)

        OTP = get_otp()
        Mob.otp = OTP
        Mob.save()
        request.session['mobile']=mobile
        return redirect('verify')
    
    return render(request,"mob.html")

def verify(request):
    mobile =request.session['mobile']
    context = {'mobile':mobile}
    if request.method == 'POST':
            otp = request.POST.get('otp')
            verify = Mobile.objects.get(mobile=mobile)

            if verify.otp==int(otp):
                Mobile.objects.filter(mobile=mobile)
                print("OTP Verify")
                request.session.set_expiry(30)
                return redirect('success_verify')  

            else:
                print("OTP galat hai")  
                return render(request,"verify.html")   
    else:
        print("Number galat hai")
    return render(request,"verify.html",context)                         

    