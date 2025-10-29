# -*- coding: utf-8 -*-
"""
Utilitaires pour calculer les statistiques et données D&D d'un personnage
"""

from .dnd_data import DND_RACES, DND_CLASSES, DND_BACKGROUNDS, DND_SKILLS

def calculate_ability_modifier(score):
    """Calcule le modificateur d'une caractéristique."""
    return (score - 10) // 2

def calculate_skills_for_character(race_key, class_key, background_key, abilities):
    """Calcule les compétences d'un personnage selon sa race, classe et historique."""
    skills = {}
    
    # Compétences de base (toutes à 0 par défaut)
    for skill_key, skill_name in DND_SKILLS.items():
        skills[skill_key] = {
            'name': skill_name,
            'proficient': False,
            'bonus': 0
        }
    
    # Compétences de l'historique
    if background_key in DND_BACKGROUNDS:
        background_skills = DND_BACKGROUNDS[background_key].get('skills', [])
        for skill_name in background_skills:
            # Trouver la clé correspondante dans DND_SKILLS
            for skill_key, full_skill_name in DND_SKILLS.items():
                if skill_name.lower() in full_skill_name.lower():
                    skills[skill_key]['proficient'] = True
                    break
    
    # Calculer les bonus (bonus de capacité + bonus de maîtrise si applicable)
    proficiency_bonus = 2  # Niveau 1
    
    ability_mapping = {
        'acrobaties': 'dexterity',
        'dressage': 'wisdom',
        'arcanes': 'intelligence',
        'athlétisme': 'strength',
        'tromperie': 'charisma',
        'histoire': 'intelligence',
        'intuition': 'wisdom',
        'intimidation': 'charisma',
        'investigation': 'intelligence',
        'médecine': 'wisdom',
        'nature': 'intelligence',
        'perception': 'wisdom',
        'représentation': 'charisma',
        'persuasion': 'charisma',
        'religion': 'intelligence',
        'escamotage': 'dexterity',
        'discrétion': 'dexterity',
        'survie': 'wisdom'
    }
    
    for skill_key, skill_data in skills.items():
        ability = ability_mapping.get(skill_key, 'intelligence')
        ability_modifier = calculate_ability_modifier(abilities.get(ability, 10))
        
        skill_bonus = ability_modifier
        if skill_data['proficient']:
            skill_bonus += proficiency_bonus
            
        skills[skill_key]['bonus'] = skill_bonus
    
    return skills

def get_racial_features(race_key):
    """Récupère les traits raciaux."""
    if race_key not in DND_RACES:
        return []
    
    race_data = DND_RACES[race_key]
    features = []
    
    # Traits de base
    for trait in race_data.get('traits', []):
        features.append({
            'name': trait,
            'type': 'Trait racial',
            'description': f"Trait de la race {race_data['name']}"
        })
    
    # Langues
    languages = race_data.get('languages', [])
    if languages:
        features.append({
            'name': 'Langues',
            'type': 'Racial',
            'description': f"Langues parlées: {', '.join(languages)}"
        })
    
    # Vitesse et taille
    features.append({
        'name': 'Vitesse',
        'type': 'Racial',
        'description': f"Vitesse de base: {race_data.get('speed', 30)} pieds"
    })
    
    features.append({
        'name': 'Taille',
        'type': 'Racial',
        'description': f"Taille: {race_data.get('size', 'Moyenne')}"
    })
    
    return features

def get_class_features(class_key, level=1):
    """Récupère les capacités de classe."""
    if class_key not in DND_CLASSES:
        return []
    
    class_data = DND_CLASSES[class_key]
    features = []
    
    # Points de vie
    hit_die = class_data.get('hit_die', 8)
    features.append({
        'name': 'Points de vie',
        'type': 'Classe',
        'description': f"Dé de vie: d{hit_die}, PV au niveau 1: {hit_die} + modificateur de Constitution"
    })
    
    # Jets de sauvegarde
    saves = class_data.get('saving_throws', [])
    if saves:
        features.append({
            'name': 'Jets de sauvegarde',
            'type': 'Classe',
            'description': f"Maîtrise des jets de sauvegarde: {', '.join(saves)}"
        })
    
    return features

def get_background_features(background_key):
    """Récupère les aptitudes d'historique."""
    if background_key not in DND_BACKGROUNDS:
        return []
    
    background_data = DND_BACKGROUNDS[background_key]
    features = []
    
    # Aptitude spéciale
    feature_name = background_data.get('feature', '')
    if feature_name:
        features.append({
            'name': feature_name,
            'type': 'Historique',
            'description': f"Aptitude d'historique {background_data['name']}"
        })
    
    return features

def get_starting_equipment(class_key, background_key):
    """Récupère l'équipement de départ."""
    equipment = []
    
    # Équipement de classe (simplifié)
    class_equipment = {
        'guerrier': ['Armure d\'écailles', 'Épée longue', 'Bouclier', 'Arbalète légère avec 20 carreaux'],
        'magicien': ['Dague', 'Sac à composantes', 'Livre de sorts', 'Armure de cuir'],
        'voleur': ['Armure de cuir', 'Épée courte', 'Outils de voleur', 'Arc court avec 20 flèches'],
        'clerc': ['Armure d\'écailles', 'Bouclier', 'Masse d\'armes', 'Symbole sacré'],
        'ranger': ['Armure de cuir clouté', 'Épée courte', 'Arc long avec 20 flèches'],
        # Ajouter d'autres classes...
    }
    
    # Équipement d'historique (simplifié)
    background_equipment = {
        'noble': ['Vêtements fins', 'Chevalière', 'Parchemin de lignage', 'Bourse avec 25 po'],
        'criminel': ['Pied-de-biche', 'Vêtements sombres avec capuche', 'Bourse avec 15 po'],
        'érudit': ['Bouteille d\'encre', 'Plume', 'Petit couteau', 'Lettres d\'un collègue décédé'],
        # Ajouter d'autres historiques...
    }
    
    # Ajouter l'équipement de classe
    class_key_lower = class_key.lower() if class_key else ''
    for key, items in class_equipment.items():
        if key in class_key_lower:
            equipment.extend(items)
            break
    
    # Ajouter l'équipement d'historique
    background_key_lower = background_key.lower() if background_key else ''
    for key, items in background_equipment.items():
        if key in background_key_lower:
            equipment.extend(items)
            break
    
    # Équipement de base
    if not equipment:
        equipment = ['Vêtements de voyage', 'Sac à dos', 'Rations (2 jours)', 'Bourse avec 10 po']
    
    return equipment

def apply_racial_bonuses(abilities, race_key):
    """Applique les bonus raciaux aux caractéristiques."""
    if race_key not in DND_RACES:
        return abilities
    
    race_data = DND_RACES[race_key]
    bonuses = race_data.get('ability_bonuses', {})
    
    for ability, bonus in bonuses.items():
        if ability in abilities:
            abilities[ability] += bonus
    
    return abilities