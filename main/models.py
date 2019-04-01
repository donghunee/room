from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class Upload(models.Model):
    username = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    person = models.CharField(max_length=50)
    attention = models.CharField(max_length=50)
    one = models.CharField(max_length=50,default="")
    two = models.CharField(max_length=50,default="")
    thr = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.username
