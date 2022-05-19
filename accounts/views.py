from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_viwe(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request,'accounts/login.html')


def logout_viwe(request):
    pass


def signup_viwe(request):
    return render(request,'accounts/signup.html')
