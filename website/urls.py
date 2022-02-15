from django.urls import path
from website.views import Home , About , Contact

urlpatterns = [

    path('',Home),
    path('about',About),
    path('contact', Contact)
]