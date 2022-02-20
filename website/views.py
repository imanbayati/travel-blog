from django.shortcuts import render


def Home(request):
    return render(request , 'website/index.html')

def About(request):
    return render(request , 'website/about.html')

def Contact(request):
    return render(request , 'website/contact.html')
