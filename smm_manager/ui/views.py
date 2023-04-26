from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    resp = "hello {}".format(request.user.get_username()) 
    return render(request, "base_generic.html")