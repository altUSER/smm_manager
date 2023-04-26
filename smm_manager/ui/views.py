from django.shortcuts import render
from django.http import HttpResponse

def delayed_posts(request):
    return render(request, 'delayed_posts.html')

def published_posts(request):
    return render(request, 'published_posts.html')

def new_publication(request):
    return render(request, 'new_publication.html')

def settings(request):
    return render(request, 'settings.html')

#def login(request):
#    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')