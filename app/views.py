from django.shortcuts import render
from django.contrib.auth.models import User, auth

# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):
    '''
        if request.method == 'POST': 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        else:
            '''
    return render(request, "register.html")

