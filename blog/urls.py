from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [
    path('',Blog_index,name='index'),
    path('<int:pid>',Blog_single,name='single'),
    path('author/<str:author_username>',Blog_index,name='author'),
    path('search/',Blog_search,name='search'),
    path('category/<str:cat_name>',Blog_index,name='category'),
    path('tag/<str:tag_name>',Blog_index,name='tag'),
]