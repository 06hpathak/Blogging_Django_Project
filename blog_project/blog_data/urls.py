from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog_data'

urlpatterns = [
    
   path('data_blog',views.data_blog,name='data_blog'),
   path('success',views.success,name='success'),
    path('success_login',views.success_login,name='success_login'),
   
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)