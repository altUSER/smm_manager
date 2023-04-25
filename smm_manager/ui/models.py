from django.db import models

class Bot(models.Model):
    auth_token = models.CharField(max_length=64)
    chanell_id = models.IntegerField()
