from django.urls import path
from website.views import Home , About , Contact , Test
app_name = 'website'
urlpatterns = [

    path('',Home,name='home'),
    path('about',About,name='about'),
    path('contact', Contact,name='contact'),
    path('test',Test)
]