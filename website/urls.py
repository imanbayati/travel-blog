from django.urls import path
from website.views import *
app_name = 'website'
urlpatterns = [

    path('',Home,name='home'),
    path('about',About,name='about'),
    path('contact', Contact,name='contact'),
    path('test',Test,name='test'),
    path('newsletter',Newsletter,name='newsletter'),
    
]