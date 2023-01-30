from django.db import models

from .race import race
from .user import user
from .equipment import equipment

class character(models.Model):
  uid = models.ForeignKey(user, on_delete=models.CASCADE)
  name = models.CharField(max_length=55)
  level = models.CharField(max_length=55)
  race = models.ForeignKey(race, on_delete=models.CASCADE)
  ability = models.CharField(max_length=55)
  description = models.CharField(max_length=55)
  equipment = models.ForeignKey(equipment, on_delete=models.CASCADE)
  spells = models.CharField(max_length=55)
  alive = models.BooleanField(default=True)
  @property
  def charclasses(self):
      charclasses = [classes for classes in self.character_classes.all()]
      return charclasses