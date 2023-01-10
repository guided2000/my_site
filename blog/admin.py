from django.contrib import admin
from blog.models import post,category,Newsletter
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class postAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','counted_views','status','published_date','created_date','updated_date')
    list_filter = ('status','author')
    ordering = ['-created_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)
    

admin.site.register(post,postAdmin)
admin.site.register(category)
admin.site.register(Newsletter)
