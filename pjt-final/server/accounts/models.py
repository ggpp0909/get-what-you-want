from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    profile_image = models.TextField(null=True)
    first_name = None
    last_name = None

    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    pass
