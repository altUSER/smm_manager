from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from ui.models import Bot
from django.contrib.auth.models import User

@login_required
def delayed_posts(request):
    return render(request, 'delayed_posts.html')

@login_required
def redirect_to_del_post(request):
    return redirect('/delayed_posts')

@login_required
def published_posts(request):
    return render(request, 'published_posts.html')

@login_required
def new_publication(request):
    return render(request, 'new_publication.html')

@login_required
def settings(request):
    try:
        bot = Bot.objects.get(owner=request.user)
        print(bot.id)
    except ObjectDoesNotExist:
        print("Bot do not exsist")
    except Exception as e:
        print(e)
    return render(request, 'settings.html')
