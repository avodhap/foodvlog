from django.contrib import messages
from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
         first_name=request.POST['firstname']
         last_name = request.POST['lastname']
         username=request.POST['username']
         email=request.POST['email']
         password=request.POST['password1']
         password2=request.POST['password2']
         if password==password2:
             if User.objects.filter(username=username).exists():
                 messages.info(request,"username taken")
                 return redirect('register')
             elif User.objects.filter(email=email).exists():
                 messages.info(request,"email taken")
                 return redirect('register')
             else:
                 myuser=User.objects.create_user(username=username,email=email,last_name=last_name,first_name=first_name,password=password)
                 myuser.save();
                 print("user created")
         else:
              print("password not matched")
              return redirect('register')
         return redirect('/')
    else:
            return render(request,'register.html')

def logout(request):
     auth.logout(request)
     return redirect('/')