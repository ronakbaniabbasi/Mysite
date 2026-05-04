from django.contrib import admin
from django.urls import path
from website.views import http_test

urlpatterns = [
    path('http-test', http_test),
    path('home', index_view),
    path('contact', contact_view),
    path('about', about_view),
    
]