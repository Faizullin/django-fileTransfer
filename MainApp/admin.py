from django.contrib import admin

# Register your models here.
from .models import FileModel

class FileModelAdmin(admin.ModelAdmin):
	list_display = ('id','title','sender','time_create','time_update','file')
	list_display_links=('id','title')
	search_fields=('title','file','sender')
	list_filter = ('time_update','time_create')
admin.site.register(FileModel,FileModelAdmin)