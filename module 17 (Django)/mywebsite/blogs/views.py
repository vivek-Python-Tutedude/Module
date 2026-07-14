from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request) :
    return HttpResponse('Home page of our Blogs')
    
def blogposts(request) :
    return HttpResponse('All blog posts!')

def python_intro(request) :
    return HttpResponse('Python Post')

def django_basic(request) :
    return HttpResponse('Django basics blog posts')