from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers

from ui.models import Post


@login_required
def delayed_posts(request):
    return render(request, 'delayed_posts.html')

@login_required
def redirect_to_del_post(request):
    return redirect('/delayed_posts')

@login_required
def published_posts(request):
    return render(request, 'published_posts.html')
