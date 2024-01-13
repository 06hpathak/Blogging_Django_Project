from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import *
from .models import *

def success(request):
    
    data= Blog_content.objects.all() 
    print(data)
    return render(request,'blog_main/data_view.html',{'data': data})

def success_login(request):
    
    data= Blog_content.objects.filter(user__id = request.user.id)
    print(data)
    return render(request,'blog_main/data_view_login.html',{'data': data})


def data_blog(request):
    if request.method == 'POST':
        print('demo')
        form =BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form_p =form.save(commit=False)
            form_p.user = request.user
            form_p.save()
            return HttpResponseRedirect(reverse('blog_data:success_login'))
        else:
            print(form.errors)
    else:
        form = BlogForm()
    return render(request, 'blog_main/blog_content.html', {'form': form})

