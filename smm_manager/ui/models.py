from django.db import models

from django.contrib.auth.models import User

class Bot(models.Model):
    auth_token = models.CharField(max_length=64)
    chanell_id = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class Post(models.Model):
    post_title = models.CharField(max_length=256)
    post_text = models.TextField()
    is_published = models.BooleanField()
    planned_publication_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)