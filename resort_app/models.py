from django.db import models

class Resort_info(models.Model):
    resort_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)
    lon = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)
    radius = models.FloatField(default=0)
    resortHomeUrl = models.CharField(max_length=255)
    url_naver = models.CharField(max_length=255)
    url_webcam = models.CharField(max_length=255)
    url_slope = models.CharField(max_length=255)
    url_bus = models.CharField(max_length=255)

class Slope_info(models.Model):
    slope_id = models.AutoField(primary_key=True)
    resort_id = models.ForeignKey(Resort_info, on_delete=models.SET_NULL, null=True, blank=True)
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)
    lon = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)
    radius = models.FloatField(default=0)
    slope_avg = models.FloatField(default=0)
    length = models.FloatField(default=0)
    score = models.FloatField(default=0)

class Reset_point(models.Model):
    reset_point_id = models.AutoField(primary_key=True)
    resort_id = models.ForeignKey(Resort_info, on_delete=models.SET_NULL, null=True, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)
    lon = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)
    radius = models.FloatField(default=0)

class Respawn_point(models.Model):
    reset_point_id = models.AutoField(primary_key=True)
    resort_id = models.ForeignKey(Resort_info, on_delete=models.SET_NULL, null=True, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)
    lon = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)
    radius = models.FloatField(default=0)
