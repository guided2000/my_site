from django.contrib import admin
from website.models import contact

# Register your models here.

class contactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','subject','created_date','updated_date','email')
    ordering = ['-created_date']
    search_fields = ['name','subject','message','email']
    list_filter = ('email','name')
admin.site.register(contact,contactAdmin)