from django.db import models

class ResortInfo(models.Model):
    resortNum = models.IntegerField(default=1)
    fullName=models.CharField(max_length=100)
    nickName=models.CharField(max_length=100)
    latitude=models.DecimalField(max_digits=10,decimal_places=7)
    longitude=models.DecimalField(max_digits=10,decimal_places=7)
    resortHomeUrl=models.CharField(max_length=255)
    webcamUrl=models.CharField(max_length=255)
    slopeUrl=models.CharField(max_length=255)
    naverUrl=models.CharField(max_length=255)
    busUrl =models.CharField(max_length=255)

    def __str__(self):
        return self.nickName
