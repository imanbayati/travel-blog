from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from blog.models import Post

# Create your views here.
def Blog_index(request,cat_name=None,author_username=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def Blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,id=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

#def Blog_category(request,cat_name):
    #posts = Post.objects.filter(status=1)
    #posts = posts.filter(category__name=cat_name)
    #context = {'posts': posts}
    #return render(request,'blog/blog-home.html',context)