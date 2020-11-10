from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mob = models.CharField(max_length=12, default='')

class Post(models.Model):
    title = models.CharField(max_length=150)

