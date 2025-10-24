from django.db import models

# Create your models here.
class Universe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    system = models.CharField(max_length=100, help_text="Ex: D&D 5e, Appel de Cthulu, Pathfinder...")
    created_at = models.DateTimeField(auto_now_add=True)

    # Nouveau champ pour stocker les règles de création spécifiques à l'univers.
    # Exemples possibles : {"classes": ["Guerrier","Mage"], "races": ["Humain","Elfe"], "levels": [1,2,3]}
    creation_rules = models.JSONField(blank=True, null=True, default=dict, help_text="JSON définissant les règles de création de personnages pour cet univers")

    def __str__(self):
        return f"{self.name} ({self.system})" if self.system else self.name

