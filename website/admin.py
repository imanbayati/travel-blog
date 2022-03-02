from django.contrib import admin
from website.models import Contact
# Register your models here.

class ContantAdmin(admin.ModelAdmin):
    search_fields = ('subject', 'name')
    filter_fields = ('email',)
    list_display = ('name','subject','email')
    date_hierarchy = 'created_date'

admin.site.register(Contact,ContantAdmin)