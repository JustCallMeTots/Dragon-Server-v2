from django.db import models

from .character import character

from .classes import classes

class charclass(models.Model):
    class_id = models.ForeignKey(classes, on_delete=models.CASCADE)
    character_id = models.ForeignKey(character, on_delete=models.CASCADE, related_name='character_classes')