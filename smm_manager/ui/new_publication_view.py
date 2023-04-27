from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateparse import parse_datetime
from smm_manager.settings import TIME_ZONE

from ui.models import Bot, Post

@login_required
def new_publication(request):
    try:
        bot = Bot.objects.get(owner=request.user)

        if request.method == "POST":
            post_title = request.POST.get("post_title")
            post_content = request.POST.get("post_content")
            post_date = parse_datetime(request.POST.get("post_date"))

            print(post_title)
            print(post_content)
            print(post_date)

            new_post = Post.objects.create(post_title=post_title, post_text=post_content, planned_publication_date=post_date, owner=request.user)

        return render(request, 'new_publication.html')
    
    except ObjectDoesNotExist:
        return render(request, 'new_publication_without_bot.html')
