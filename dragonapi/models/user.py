from django.db import models


class user(models.Model):

    uid = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)