from django.db import models
from user_app.models import User
from resort_app.models import Slope_info

class Slope_pass_temp(models.Model):
    slope_pass_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    slope_id = models.ForeignKey(Slope_info, null=False, on_delete=models.CASCADE)
    pass_time = models.DateTimeField(auto_now=True)

class Ranking_record(models.Model):
    ranking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    slope_id = models.ForeignKey(Slope_info, null=False, on_delete=models.CASCADE)
    pass_time = models.DateTimeField()
