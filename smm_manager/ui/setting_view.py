from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from ui.models import Bot

@login_required
def settings(request):
    if request.method == "POST":


        try:
            auth_token = request.POST.get("bot_token") # <64 char
            chanell_id = int(request.POST.get("channel_id")) # >8 and <12 chars in int

            if len(auth_token) <= 64:

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
                
            else:
                data = {"status": "Некорректные данные"}
                return render(request, 'settings.html', context=data)
        except:
            data = {"status": "Некорректные данные"}
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