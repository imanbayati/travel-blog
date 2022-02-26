from django.db import models

# Create your models here.

class Contact(models.Model):
    
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    massage = models.TextField()