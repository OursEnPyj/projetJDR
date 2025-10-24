from django.db import models
from universes.models import Universe
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Character(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, related_name='characters')
    name = models.CharField(max_length=120)
    race = models.CharField(max_length=80, blank=True)
    char_class = models.CharField(max_length=80, blank=True)


# Caractéristiques simples (exemple)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)


    description = models.TextField(blank=True)
    background = models.TextField(blank=True)


    created_at = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['name']


def __str__(self):
    return f"{self.name} ({self.universe.name})"