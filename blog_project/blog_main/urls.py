from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog_main'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.user_register, name='user_register'),
    path('user_login', views.user_login, name='user_login'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    
   
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)