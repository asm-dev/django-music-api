from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    favorite_songs = models.ManyToManyField('Song', blank=True)
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Song(models.Model):
    title = models.CharField(max_length=255, blank=False)
    artist = models.CharField(max_length=255, blank=True)
    album = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
