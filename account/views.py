from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.

def register(request):
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()  
    return render(request,'registration.html',{'form':form}) 

def user_login(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            
            login(request,user)
            print(request.user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

    

