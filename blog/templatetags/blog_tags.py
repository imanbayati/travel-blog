from django import template

from blog.models import Post

register = template.Library()

@register.simple_tag

def countpost():
    posts = Post.objects.filter(status=1)
    return posts