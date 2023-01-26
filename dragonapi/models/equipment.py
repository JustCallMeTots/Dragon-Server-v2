from django.db import models

class equipment(models.Model):
    weapon_name = models.CharField(max_length=55)
    weapon_type = models.CharField(max_length=55)
    weapon_description = models.CharField(max_length=55)