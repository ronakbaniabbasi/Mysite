from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_view (request):
    return render (request, 'Websitee/index.html')

def about_view (request):
    return render (request, 'Websitee/about.html')

def contact_view (request):
    return render (request, 'Websitee/contact.html')

def test_view (request):
    context = {'name': 'Ronak', 'last_name':'Baniabbasi'}
    return render (request, 'Websitee/test.html', context)
