from django.db import models

# Create your models here.

class UserInfor2(models.Model):
    username=models.CharField(max_length=64)
    sex=models.CharField(max_length=64)
    email=models.CharField(max_length=64)