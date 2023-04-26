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
    if request.POST:
        auth_token = request.POST.get("bot_token")
        chanell_id = request.POST.get("channel_id")

        print(auth_token, chanell_id)
        try:
            bot = Bot.objects.get(owner=request.user)
            bot.auth_token = auth_token
            bot.chanell_id = chanell_id
            bot.save()
            data = {"auth_token": auth_token, "channel_id": chanell_id, "status": "Данные приняты"}
            return render(request, "settings.html", context=data)
        except ObjectDoesNotExist:
            bot = Bot.objects.create(auth_token=auth_token, chanell_id=chanell_id, owner=request.user)
            bot.save()
            data = {"auth_token": auth_token, "channel_id": chanell_id, "status": "Данные приняты"}
            return render(request, "settings.html", context=data)
        except Exception as e:
            data = {"status": e}
            return render(request, 'settings.html', context=data)
    try:
        bot = Bot.objects.get(owner=request.user)
        data = {"auth_token": bot.auth_token, "channel_id": bot.chanell_id}
        return render(request, 'settings.html', context=data)
    except ObjectDoesNotExist:
        print("Bot do not exsist")
        return render(request, 'settings.html')
    except Exception as e:
        print(e)
        data = {"status": e}
        return render(request, 'settings.html', context=data)