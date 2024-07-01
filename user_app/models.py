from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255, unique=True)
    crew_id = models.ForeignKey('crew_app.Crew_info', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    favoriteResort = models.ForeignKey('resort_app.Resort_info', on_delete=models.SET_NULL, null=True, blank=True)  # default 제거
    
    def __str__(self):
        return self.email
