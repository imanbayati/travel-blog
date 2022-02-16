from django.shortcuts import render


def Home(request):
    return render(request , 'website/index.html')

def About(request):
    return render(request , 'website/about us.html')

def Contact(request):
    return render(request , 'website/contact us.html')
