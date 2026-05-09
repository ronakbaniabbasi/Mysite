from django.contrib import admin
from django.urls import path
from blog.views import index_view, contact_view, about_view, blog_single, blog_view

app_name = 'blog'

urlpatterns = [

    path('', index_view, name = "index"),
    path('contact', contact_view, name = "contact"),
    path('about', about_view, name = "about"),
    path('blog-home', blog_view, name = "blog-home"),
    path('blog-single', blog_single , name = "blog-single"),
    
    
]