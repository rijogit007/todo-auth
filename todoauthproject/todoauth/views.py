from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from todoauth import models
# Create your views here.

def signup(request):
    
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        # conform_password=request.POST.get("conform_password")      
        if User.objects.filter(username=username).exists():
            messages.error(request,"password does not matches")
            
            return redirect("signup")


        user=User.objects.create_user(username=username,email=email,password=password)
        
        user.save()
        
        
        messages.success(request,"Account Created successfully , please login")
        return redirect('login')
    return render(request,'login.html')




def login(request):
    
    
    
    
    return render(request,'login.html')
   
                