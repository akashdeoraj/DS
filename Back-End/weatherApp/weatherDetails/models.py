from calendar import FRIDAY
from django.db import models


class coordinateWiseData(models.Model):
    id = models.AutoField(primary_key=id)
    longitude = models.TextField(default="")
    latitude  = models.TextField(default="")
    gridId = models.TextField(default="")
    gridx = models.TextField(default="")
    gridy = models.TextField(default="")
    today = models.TextField(default="")
    tonight = models.TextField(default="")
    monday = models.TextField(default="")
    monday_night = models.TextField(default="")
    tuesday = models.TextField(default="")
    tuesday_night = models.TextField(default="")
    wednesday = models.TextField(default="")
    wednesday_night = models.TextField(default="")
    thursday = models.TextField(default="")
    thursday_night = models.TextField(default="")
    friday = models.TextField(default="")
    friday_night = models.TextField(default="")
    saturday = models.TextField(default="")
    saturday_night = models.TextField(default="")
    sunday = models.TextField(default="")
    sunday_night = models.TextField(default="")
    lastupdated = models.TextField(default="")