from django.shortcuts import render
from website.forms import NameForm , Contactform
from django.http import HttpResponse


def Home(request):
    return render(request , 'website/index.html')

def About(request):
    return render(request , 'website/about.html')

def Contact(request):
    return render(request , 'website/contact.html')

def Test(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    
    form = Contactform()
    context = {'form':form}
    return render(request,'test.html',context)