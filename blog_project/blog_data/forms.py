
from django import forms
from django.forms import fields, widgets
from .models import *
from ckeditor.fields import RichTextField

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog_content
        fields = '__all__'
        exclude = ('user', 'date')

        widgets = {
            'Blog_Title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'Blog_Description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'Blog_content': RichTextField(),
            'blog_image': forms.FileInput(attrs={
                'class': 'form-control'
            })

        }