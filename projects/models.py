from django.db import models
# this is setting up my main database
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery')
    link_git = models.URLField(max_length=200, null=True)
    link_view = models.URLField(max_length=200, null=True)
    
