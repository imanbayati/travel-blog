from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [

    path('',Blog_index,name='index'),
    path('single',Blog_single,name='single'),

]