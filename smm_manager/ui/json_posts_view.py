from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ui.models import Post
from django.core import serializers
import json

@login_required
def get_json_delayed_posts(request):
    page = int(request.GET.get('page', 1)) # используем значение по умолчанию, если параметр не задан
    limit = int(request.GET.get('limit', 10)) # используем значение по умолчанию, если параметр не задан

    start_index = (page - 1) * limit
    end_index = start_index + limit

    posts_data = Post.objects.filter(owner=request.user, is_published=False).values()[start_index:end_index]

    posts = [Post(**data) for data in posts_data]
    print("test")
    print(posts)
    serialized_objects = serializers.serialize('json', posts)
    deserialized_objects = json.loads(serialized_objects)

    for post in deserialized_objects:
        time_string = post["fields"]["planned_publication_date"]
        formated_time_string = time_string[:time_string.find("T")] + " " + time_string[time_string.find("T")+1:len(time_string)-1]
        post["fields"]["planned_publication_date"] = formated_time_string

    serialized_objects = json.dumps(deserialized_objects)
    return HttpResponse(serialized_objects, content_type='application/json')

@login_required
def get_json_published_posts(request):
    page = int(request.GET.get('page', 1)) # используем значение по умолчанию, если параметр не задан
    limit = int(request.GET.get('limit', 10)) # используем значение по умолчанию, если параметр не задан

    start_index = (page - 1) * limit
    end_index = start_index + limit

    posts_data = Post.objects.filter(owner=request.user, is_published=True).values()[start_index:end_index]

    posts = [Post(**data) for data in posts_data]
    serialized_objects = serializers.serialize('json', posts)
    deserialized_objects = json.loads(serialized_objects)

    for post in deserialized_objects:
        time_string = post["fields"]["planned_publication_date"]
        formated_time_string = time_string[:time_string.find("T")] + " " + time_string[time_string.find("T")+1:len(time_string)-1]
        post["fields"]["planned_publication_date"] = formated_time_string

    serialized_objects = json.dumps(deserialized_objects)
    return HttpResponse(serialized_objects, content_type='application/json')