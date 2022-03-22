from django.shortcuts import render
from website.forms import NameForm
from django.http import HttpResponse


def Home(request):
    return render(request , 'website/index.html')

def About(request):
    return render(request , 'website/about.html')

def Contact(request):
    return render(request , 'website/contact.html')

def Test(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email'] 
            subject = form.cleaned_data['subject'] 
            message = form.cleaned_data['message'] 
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    
    form = NameForm()
    context = {'form':form}
    return render(request,'test.html',context)