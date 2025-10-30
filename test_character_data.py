#!/usr/bin/env python3
"""
Script de test pour ajouter des données d'exemple à un personnage
pour tester l'interface de modification des skills, features et équipement.
"""

import os
import sys
import django

# Configuration Django
sys.path.append('/home/useradm/Bureau/projetJDR/mj_app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mj_app.settings')
django.setup()

from characters.models import Character

def add_test_data():
    """Ajoute des données de test à un personnage existant."""
    try:
        # Chercher un personnage existant (ID 17 par exemple)
        character = Character.objects.get(pk=17)
        print(f"Ajout de données de test pour le personnage : {character.name}")
        
        # Données de test pour les compétences
        test_skills = {
            "Acrobatie": {"bonus": 5, "proficient": True, "expert": False},
            "Athlétisme": {"bonus": 3, "proficient": False, "expert": False},
            "Discrétion": {"bonus": 8, "proficient": True, "expert": True},
            "Investigation": {"bonus": 6, "proficient": True, "expert": False},
            "Perception": {"bonus": 4, "proficient": False, "expert": False},
            "Persuasion": {"bonus": 7, "proficient": True, "expert": False}
        }
        
        # Données de test pour les capacités
        test_features = [
            {
                "name": "Vision dans le noir",
                "description": "Voir jusqu'à 18 mètres dans l'obscurité totale",
                "source": "Elfe"
            },
            {
                "name": "Sens aiguisés",
                "description": "Avantage aux jets de Perception liés à l'ouïe ou la vue",
                "source": "Elfe"
            },
            {
                "name": "Action défensive",
                "description": "Utiliser une action bonus pour gagner +1 CA jusqu'au prochain tour",
                "source": "Guerrier"
            },
            {
                "name": "Second souffle",
                "description": "Récupérer 1d10+1 points de vie en utilisant une action bonus",
                "source": "Guerrier"
            }
        ]
        
        # Données de test pour l'équipement
        test_equipment = [
            "Épée longue +1",
            "Armure de cuir clouté",
            "Bouclier",
            "Arc court elfique avec 60 flèches",
            "Corde en soie (15 mètres)",
            "Kit d'escalade",
            "Rations pour 5 jours",
            "Outre d'eau",
            "Sac de couchage",
            "50 pièces d'or",
            "25 pièces d'argent"
        ]
        
        # Données de test pour les langues
        test_languages = [
            "Commun",
            "Elfique",
            "Orc",
            "Draconique"
        ]
        
        # Mise à jour du personnage
        character.skills = test_skills
        character.features = test_features
        character.equipment = test_equipment
        character.languages = test_languages
        
        character.save()
        
        print("✅ Données de test ajoutées avec succès !")
        print(f"- {len(test_skills)} compétences")
        print(f"- {len(test_features)} capacités")
        print(f"- {len(test_equipment)} objets d'équipement")
        print(f"- {len(test_languages)} langues")
        
    except Character.DoesNotExist:
        print("❌ Erreur : Personnage avec l'ID 17 non trouvé")
    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    add_test_data()