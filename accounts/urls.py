from django.urls import path
from accounts.views import *
app_name = 'accounts'
urlpatterns = [
    path('login',login_viwe,name='login'),
    path('logout',logout_viwe,name='logout'),
    path('signup',signup_viwe,name='signup')
]