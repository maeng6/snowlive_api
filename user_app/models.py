from django.contrib.auth.models import AbstractUser
from django.db import models

from resort_app.models import ResortInfo

class CustomUser(AbstractUser):
    uid = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)  # username 필드
    email = models.EmailField(unique=True)  # email 필드 추가
    favoriteResort = models.ForeignKey(ResortInfo,default=1,on_delete=models.SET_DEFAULT)


    def __str__(self):
        return self.email
