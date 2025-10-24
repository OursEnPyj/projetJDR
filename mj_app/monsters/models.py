from django.db import models

# Create your models here.

class Monster(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    hit_points = models.IntegerField(default=10)
    armor_class = models.IntegerField(default=10)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name