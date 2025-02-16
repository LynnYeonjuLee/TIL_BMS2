from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    introduce = models.CharField(max_length=50, blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')