from django.contrib import admin
from . import models

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link_git', 'link_view')
    list_filter = ('title', )
    # ordering = ('title', )
    search_field = ('title')
    
admin.site.register(models.Project, ProjectAdmin)


# testing my commits
# this will make sure i can view my data table on admin page 
# this will also make adding items to my database a lot easier
