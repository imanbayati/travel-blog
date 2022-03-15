from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from blog.models import Post

# Create your views here.
def Blog_index(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def Blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,id=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

