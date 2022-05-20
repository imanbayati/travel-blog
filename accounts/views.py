from multiprocessing import context
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import AuthenticationForm

def login_viwe(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        
        form = AuthenticationForm()
        context = {'form': form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

def logout_viwe(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')
def signup_viwe(request):
    return render(request,'accounts/signup.html')
