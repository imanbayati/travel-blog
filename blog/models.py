from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=35)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
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
    
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    subject = models.CharField(max_length=225)
    email = models.EmailField()
    message = models.TextField() 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created_date',)
    
    def __str__(self):
        return self.name