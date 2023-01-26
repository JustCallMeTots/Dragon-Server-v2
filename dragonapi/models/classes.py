from django.db import models

class classes(models.Model):
    hitDie = models.CharField(max_length=55)
    saves = models.CharField(max_length=55)
    class_description = models.CharField(max_length=55)
    classes_name = models.CharField(max_length=55)