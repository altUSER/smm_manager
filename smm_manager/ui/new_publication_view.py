from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateparse import parse_datetime

from ui.models import Bot

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

        return render(request, 'new_publication.html')
    
    except ObjectDoesNotExist:
        return render(request, 'new_publication_without_bot.html')
