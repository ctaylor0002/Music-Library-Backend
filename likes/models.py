from statistics import mode
from django.db import models

# Create your models here.

class Likes(models.Model):
    song_id = models.ForeignKey("songs.Songs", on_delete=models.CASCADE, null=False)
    like_condition = models.BooleanField()