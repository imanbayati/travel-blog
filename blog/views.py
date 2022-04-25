from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def Blog_index(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs.get('cat_name'))
    if kwargs.get('author_username') !=None :
        posts = posts.filter(author__username=kwargs.get('author_username'))
    if kwargs.get('tag_name') != None:
        posts = Post.objects.filter(tags__name__in=[kwargs.get('tag_name')])
    posts = Paginator(posts,4)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def Blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,id=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

def Blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if search := request.GET.get('s'):
            posts = posts.filter(content__contains=search)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)