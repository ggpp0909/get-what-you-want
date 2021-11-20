from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=10, unique=True)
    profile_image = models.TextField(null=True)
    first_name = None
    last_name = None

    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    def __str__(self):
        return self.username

class Feedback(models.Model):
    user = models.TextField()
    feedback = models.TextField()

    def __str__(self):
        return self.feedback