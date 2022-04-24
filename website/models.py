from django.db import models
from django.contrib.sites.models import Site 

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
    
    
class Newsletter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email
    
#class site(models.Model):
    #sites = models.ManyToManyField(Site)