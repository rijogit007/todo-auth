from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from todoauth import models
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        # conform_password=request.POST.get("conform_password")      
        if User.objects.filter(username=username).exists():
            messages.error(request,"username already exists")
            
            return redirect("signup")


        user=User.objects.create_user(username=username,email=email,password=password)
        
        user.save()
        
        
        messages.success(request,"Account Created successfully , please login")
        return redirect('login')
    return render(request,'signup.html')




def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
            messages.success(request,"password doesnt match plese try again")
            
        else:
            return redirect('login')
        
            messages.error(request,"password doesnt match plese try again")
    
    
    
    return render(request,'login.html')
   
                
@login_required
def homepage(request):
        
        return render(request,'todopage.html')            