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
    level = models.IntegerField(default=1)

    # Caractéristiques
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

    # Historique D&D (Noble, Criminel, etc.)
    dnd_background = models.CharField(max_length=80, blank=True, verbose_name="Historique D&D")
    
    # Background narratif du personnage (histoire personnelle)
    background_story = models.TextField(blank=True, verbose_name="Histoire personnelle")
    
    # Description physique
    description = models.TextField(blank=True)

    # Compétences (stockées en JSON pour flexibilité)
    skills = models.JSONField(default=dict, blank=True, help_text="Compétences et leurs bonus")
    
    # Équipement (stocké en JSON)
    equipment = models.JSONField(default=list, blank=True, help_text="Liste d'équipements")
    
    # Traits et capacités spéciales (stockés en JSON)
    features = models.JSONField(default=list, blank=True, help_text="Traits raciaux, capacités de classe, etc.")
    
    # Langues connues
    languages = models.JSONField(default=list, blank=True, help_text="Langues parlées")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.universe.name})"