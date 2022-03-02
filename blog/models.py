from django.db import models

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length = 220) 
    content = models.TextField()
    status = models.BooleanField(default=False)
    counted_view = models.IntegerField(default=0)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ['created_date','status']
    
    def __str__(self):
        return  '{} - {}'.format(self.title,self.id)
    
