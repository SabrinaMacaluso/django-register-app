from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
       
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("success")
                return redirect('login_user')
   
    return render(request, "register.html")


def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        else: 
            messages.info(request, 'Username or Password is Wrong')
            return redirect('login_user')
    else:
        return render(request, "login.html")

def logout_user(request):
    auth.logout(request)
    return redirect('home')


def contact(request):
    return render(request, 'contact.html')