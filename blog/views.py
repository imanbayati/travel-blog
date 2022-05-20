from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your message submited')
        else:
             messages.add_message(request, messages.ERROR, 'your message not submited')
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,id=pid)
    comments = Comment.objects.filter(post=post.id,approved=True)
    form = CommentForm()
    context = {'post':post,'comments':comments,'form':form}
    if post.login_require == False:
        return render(request,'blog/blog-single.html',context)
    else:
        if request.user.is_authenticated:
            return render(request,'blog/blog-single.html',context)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))

def Blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if search := request.GET.get('s'):
            posts = posts.filter(content__contains=search)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)