from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    profile_image = models.TextField()
    
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    pass
