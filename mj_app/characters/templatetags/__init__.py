# -*- coding: utf-8 -*-
"""
Template tags et filtres personnalisés pour les personnages
"""

from django import template

register = template.Library()

@register.filter
def ability_modifier(value):
    """Calcule le modificateur d'une caractéristique D&D."""
    try:
        score = int(value)
        modifier = (score - 10) // 2
        return modifier
    except (ValueError, TypeError):
        return 0

@register.filter
def modifier_display(value):
    """Affiche le modificateur avec le signe + ou -."""
    modifier = ability_modifier(value)
    if modifier >= 0:
        return f"+{modifier}"
    else:
        return str(modifier)

@register.filter
def get_item(dictionary, key):
    """Récupère un élément d'un dictionnaire par sa clé."""
    try:
        return dictionary.get(key)
    except (AttributeError, TypeError):
        return None