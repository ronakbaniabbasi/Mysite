from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render (request, 'Blogg/index.html')

def about_view(request):
    return render (request, 'Blogg/about.html')

def contact_view(request):
    return render (request, 'Blogg/contact.html')

def blog_view(request):
    return render (request, 'Blogg/blog-home.html')

def blog_single(request):
    return render (request, 'Blogg/blog-single.html')

