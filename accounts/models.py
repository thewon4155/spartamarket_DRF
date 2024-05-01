from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)