from django import template

from blog.models import Post

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
    posts = Post.objects.filter(status=1).order_by('published_date')
    return {'posts':posts}