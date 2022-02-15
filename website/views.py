from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Home(request):
    return HttpResponse('home page')

def About(request):
    return HttpResponse('about page')

def Contact(request):
    return HttpResponse('contact page')