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

# def get_json_published_posts(request):
#     posts = Post.objects.filter(owner = request.user).values()
#     print(posts)
#     serialized_objects = serializers.serialize('json', posts)
#     print(serialized_objects)
#     return HttpResponse(serialized_objects, content_type='application/json')

#def get_json_published_posts(request):
#    posts_data = Post.objects.filter(owner=request.user).values()
#    posts = [Post(**data) for data in posts_data]
#    serialized_objects = serializers.serialize('json', posts)
#    return HttpResponse(serialized_objects, content_type='application/json')

def get_json_published_posts(request):
    page = int(request.GET.get('page', 1)) # используем значение по умолчанию, если параметр не задан
    limit = int(request.GET.get('limit', 10)) # используем значение по умолчанию, если параметр не задан

    start_index = (page - 1) * limit
    end_index = start_index + limit

    posts_data = Post.objects.filter(owner=request.user, ).values()[start_index:end_index]
    posts = [Post(**data) for data in posts_data]
    serialized_objects = serializers.serialize('json', posts)
    return HttpResponse(serialized_objects, content_type='application/json')