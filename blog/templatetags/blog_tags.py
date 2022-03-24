from django import template

from blog.models import Post,Category

from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag

def countpost():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter

def snippets(value):
    return value[:200] +' ' + '. . .'


@register.inclusion_tag('blog/blog-populer-post.html')

def popular():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:4]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-posts-category.html')

def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return{'categories':cat_dict}




    

