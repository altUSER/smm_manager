#setup Django ORM
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'smm_manager.settings'
django.setup()

from ui.models import Post, Bot
from django.utils import timezone
import telebot
from time import sleep

#--settimgs--
sleep_time=0.1      #time before check posts in seconds
time_delta = 10  #time window four post
DEBUG=False      #disable send to telegram
#------------


def sendMsg(token, id, msg):
    bot = telebot.TeleBot(token)
    bot.send_message(id, msg)

def check_and_publicate_post():
    post_for_publicate = Post.objects.filter(is_published=False)

    for post in post_for_publicate:
        delta = timezone.now() - post.planned_publication_date
        if abs(delta.total_seconds()) < time_delta:
            owner = post.owner
            bot = Bot.objects.get(owner=owner)
            print("Find post 4 pub:", post.post_title, "bot id:", bot.id)

            if not DEBUG:
                sendMsg(bot.auth_token, bot.chanell_id, post.post_text)

            post.is_published = True
            post.save()

if __name__ == "__main__":
    while True:
        check_and_publicate_post()
        sleep(0.1)