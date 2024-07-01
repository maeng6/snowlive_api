from django.db import models

class Crew_info(models.Model):
    crew_id = models.AutoField(primary_key=True)
    crew_name = models.CharField(max_length=255)
    crew_logo_url = models.CharField(max_length=255)
    base_resort_id = models.ForeignKey('resort_app.Resort_info', on_delete=models.SET_NULL, null=True, blank=True)  # default 제거
    iskusbf = models.BooleanField(default=False)
    notice = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
