from django.contrib import admin
from blog.models import Post,Category,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('title','author','status','counted_view','published_date','created_date')
    list_filter = ('status',)
    search_fields = ['title','content']
    
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('name','post','approved','created_date')
    list_filter = ('approved','post')
    search_fields = ['name','subject'] 
admin.site.register(Post,PostAdmin)


admin.site.register(Category) 

admin.site.register(Comment,CommentAdmin)