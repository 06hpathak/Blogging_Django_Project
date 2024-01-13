from django.contrib.auth.models import update_last_login
from django.db import models
from blog_main.models import User

from ckeditor.fields import RichTextField
# Create your models here.

class Blog_content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    Blog_Title = models.CharField(max_length=120)
    Blog_Description = models.CharField(max_length=120)
    Blog_image = models.ImageField(upload_to='blog_image')
    Blog_content =  RichTextField(blank=True,null=True)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
