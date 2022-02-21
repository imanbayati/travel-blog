from django.shortcuts import render

# Create your views here.
def Blog_index(request):
    return render(request,'blog/blog-home.html')

def Blog_single(request):
    return render(request,'blog/blog-single.html')