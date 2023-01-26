from django.db import models

class race(models.Model):
    race_name = models.CharField(max_length=55)
    race_description = models.CharField(max_length=55)
    ability_increase = models.CharField(max_length=55)