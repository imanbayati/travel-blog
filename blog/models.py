from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=35)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length = 220) 
    content = models.TextField()
    status = models.BooleanField(default=False)
    counted_view = models.IntegerField(default=0)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return  self.title 
    
