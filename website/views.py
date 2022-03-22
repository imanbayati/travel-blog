from django.shortcuts import render
from website.forms import NameForm , Contactform , Newsletterform
from django.http import HttpResponse , HttpResponseRedirect


def Home(request):
    return render(request , 'website/index.html')

def About(request):
    return render(request , 'website/about.html')

def Contact(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
    form = Contactform()
    context = {'form': form} 
    return render(request , 'website/contact.html',context)



def Newsletter(request):
    if request.method=='POST':
        form = Newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    

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