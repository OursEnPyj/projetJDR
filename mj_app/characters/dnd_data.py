# -*- coding: utf-8 -*-
"""
Données D&D 5e pour la création de personnages
"""

# Races avec leurs modificateurs et traits
DND_RACES = {
    'humain': {
        'name': 'Humain',
        'ability_bonuses': {'strength': 1, 'dexterity': 1, 'constitution': 1, 'intelligence': 1, 'wisdom': 1, 'charisma': 1},
        'size': 'Moyenne',
        'speed': 30,
        'languages': ['Commun', 'Au choix'],
        'traits': ['Compétence supplémentaire', 'Don supplémentaire au niveau 1'],
        'description': 'Les humains sont une race adaptable et ambitieuse.'
    },
    'elfe': {
        'name': 'Elfe',
        'ability_bonuses': {'dexterity': 2},
        'size': 'Moyenne',
        'speed': 30,
        'languages': ['Commun', 'Elfique'],
        'traits': ['Vision dans le noir', 'Sens aiguisés', 'Ascendance féerique', 'Transe'],
        'description': 'Les elfes sont une race magique aux sens aiguisés.',
        'subraces': {
            'haut_elfe': {'name': 'Haut-Elfe', 'ability_bonuses': {'intelligence': 1}},
            'elfe_des_bois': {'name': 'Elfe des bois', 'ability_bonuses': {'wisdom': 1}},
            'elfe_noir': {'name': 'Elfe noir (Drow)', 'ability_bonuses': {'charisma': 1}}
        }
    },
    'nain': {
        'name': 'Nain',
        'ability_bonuses': {'constitution': 2},
        'size': 'Moyenne',
        'speed': 25,
        'languages': ['Commun', 'Nain'],
        'traits': ['Vision dans le noir', 'Résistance naine', 'Entraînement aux armes naines'],
        'description': 'Les nains sont un peuple robuste vivant dans les montagnes.',
        'subraces': {
            'nain_des_montagnes': {'name': 'Nain des montagnes', 'ability_bonuses': {'strength': 2}},
            'nain_des_collines': {'name': 'Nain des collines', 'ability_bonuses': {'wisdom': 1}}
        }
    },
    'halfelin': {
        'name': 'Halfelin',
        'ability_bonuses': {'dexterity': 2},
        'size': 'Petite',
        'speed': 25,
        'languages': ['Commun', 'Halfelin'],
        'traits': ['Chance', 'Brave', 'Agilité halfeline'],
        'description': 'Les halfelins sont un peuple petit mais courageux.',
        'subraces': {
            'pied_leger': {'name': 'Pied-léger', 'ability_bonuses': {'charisma': 1}},
            'robuste': {'name': 'Robuste', 'ability_bonuses': {'constitution': 1}}
        }
    },
    'drakéide': {
        'name': 'Drakéide',
        'ability_bonuses': {'strength': 2, 'charisma': 1},
        'size': 'Moyenne',
        'speed': 30,
        'languages': ['Commun', 'Draconique'],
        'traits': ['Ascendance draconique', 'Souffle destructeur', 'Résistance aux dégâts'],
        'description': 'Les drakéides portent l\'héritage des dragons anciens.'
    },
    'gnome': {
        'name': 'Gnome',
        'ability_bonuses': {'intelligence': 2},
        'size': 'Petite',
        'speed': 25,
        'languages': ['Commun', 'Gnome'],
        'traits': ['Vision dans le noir', 'Ruse gnome'],
        'description': 'Les gnomes sont un peuple petit mais ingénieux.',
        'subraces': {
            'gnome_des_forets': {'name': 'Gnome des forêts', 'ability_bonuses': {'dexterity': 1}},
            'gnome_des_roches': {'name': 'Gnome des roches', 'ability_bonuses': {'constitution': 1}}
        }
    },
    'demi-elfe': {
        'name': 'Demi-elfe',
        'ability_bonuses': {'charisma': 2},
        'size': 'Moyenne',
        'speed': 30,
        'languages': ['Commun', 'Elfique', 'Au choix'],
        'traits': ['Vision dans le noir', 'Ascendance féerique', 'Polyvalence'],
        'description': 'Les demi-elfes combinent les meilleurs traits des humains et des elfes.'
    },
    'demi-orc': {
        'name': 'Demi-orc',
        'ability_bonuses': {'strength': 2, 'constitution': 1},
        'size': 'Moyenne',
        'speed': 30,
        'languages': ['Commun', 'Orc'],
        'traits': ['Vision dans le noir', 'Endurance implacable', 'Attaques sauvages'],
        'description': 'Les demi-orcs luttent entre leur héritage sauvage et leur humanité.'
    },
    'tieffelin': {
        'name': 'Tieffelin',
        'ability_bonuses': {'intelligence': 1, 'charisma': 2},
        'size': 'Moyenne',
        'speed': 30,
        'languages': ['Commun', 'Infernal'],
        'traits': ['Vision dans le noir', 'Résistance infernale', 'Héritage infernal'],
        'description': 'Les tieffelins portent l\'héritage de pactes infernaux anciens.'
    }
}

# Classes avec leurs caractéristiques principales
DND_CLASSES = {
    'barbare': {
        'name': 'Barbare',
        'hit_die': 12,
        'primary_abilities': ['Force'],
        'saving_throws': ['Force', 'Constitution'],
        'skills_available': ['Dressage', 'Intimidation', 'Nature', 'Perception', 'Survie'],
        'skill_choices': 2,
        'description': 'Un guerrier féroce qui puise sa force dans la rage primitive.'
    },
    'barde': {
        'name': 'Barde',
        'hit_die': 8,
        'primary_abilities': ['Charisme'],
        'saving_throws': ['Dextérité', 'Charisme'],
        'skills_available': ['Tous'],
        'skill_choices': 3,
        'description': 'Un maître des chants, de la parole et de la magie qu\'ils contiennent.'
    },
    'clerc': {
        'name': 'Clerc',
        'hit_die': 8,
        'primary_abilities': ['Sagesse'],
        'saving_throws': ['Sagesse', 'Charisme'],
        'skills_available': ['Histoire', 'Intuition', 'Médecine', 'Persuasion', 'Religion'],
        'skill_choices': 2,
        'description': 'Un champion divin qui manie la magie divine au service d\'une puissance supérieure.'
    },
    'druide': {
        'name': 'Druide',
        'hit_die': 8,
        'primary_abilities': ['Sagesse'],
        'saving_throws': ['Intelligence', 'Sagesse'],
        'skills_available': ['Arcanes', 'Dressage', 'Intuition', 'Médecine', 'Nature', 'Perception', 'Religion', 'Survie'],
        'skill_choices': 2,
        'description': 'Un prêtre de la nature, utilisant les forces élémentaires et se transformant en bête.'
    },
    'ensorceleur': {
        'name': 'Ensorceleur',
        'hit_die': 6,
        'primary_abilities': ['Charisme'],
        'saving_throws': ['Constitution', 'Charisme'],
        'skills_available': ['Arcanes', 'Intimidation', 'Intuition', 'Persuasion', 'Religion', 'Tromperie'],
        'skill_choices': 2,
        'description': 'Un lanceur de sorts qui puise sa magie dans une source innée.'
    },
    'guerrier': {
        'name': 'Guerrier',
        'hit_die': 10,
        'primary_abilities': ['Force ou Dextérité'],
        'saving_throws': ['Force', 'Constitution'],
        'skills_available': ['Acrobaties', 'Dressage', 'Athlétisme', 'Histoire', 'Intimidation', 'Intuition', 'Perception', 'Survie'],
        'skill_choices': 2,
        'description': 'Un maître du combat martial, compétent avec une variété d\'armes et d\'armures.'
    },
    'magicien': {
        'name': 'Magicien',
        'hit_die': 6,
        'primary_abilities': ['Intelligence'],
        'saving_throws': ['Intelligence', 'Sagesse'],
        'skills_available': ['Arcanes', 'Histoire', 'Intuition', 'Investigation', 'Médecine', 'Religion'],
        'skill_choices': 2,
        'description': 'Un érudit de la magie, capable de manipuler les structures de la réalité.'
    },
    'moine': {
        'name': 'Moine',
        'hit_die': 8,
        'primary_abilities': ['Dextérité', 'Sagesse'],
        'saving_throws': ['Force', 'Dextérité'],
        'skills_available': ['Acrobaties', 'Athlétisme', 'Histoire', 'Intuition', 'Religion', 'Discrétion'],
        'skill_choices': 2,
        'description': 'Un combattant martial utilisant le pouvoir du ki pour accomplir des prouesses.'
    },
    'paladin': {
        'name': 'Paladin',
        'hit_die': 10,
        'primary_abilities': ['Force', 'Charisme'],
        'saving_throws': ['Sagesse', 'Charisme'],
        'skills_available': ['Athlétisme', 'Intuition', 'Intimidation', 'Médecine', 'Persuasion', 'Religion'],
        'skill_choices': 2,
        'description': 'Un guerrier saint lié par un serment sacré de combattre le mal.'
    },
    'rôdeur': {
        'name': 'Rôdeur',
        'hit_die': 10,
        'primary_abilities': ['Dextérité', 'Sagesse'],
        'saving_throws': ['Force', 'Dextérité'],
        'skills_available': ['Dressage', 'Athlétisme', 'Intuition', 'Investigation', 'Nature', 'Perception', 'Discrétion', 'Survie'],
        'skill_choices': 3,
        'description': 'Un guerrier de la nature, expert en traque et en survie.'
    },
    'roublard': {
        'name': 'Roublard',
        'hit_die': 8,
        'primary_abilities': ['Dextérité'],
        'saving_throws': ['Dextérité', 'Intelligence'],
        'skills_available': ['Acrobaties', 'Athlétisme', 'Tromperie', 'Intuition', 'Intimidation', 'Investigation', 'Perception', 'Représentation', 'Persuasion', 'Escamotage', 'Discrétion'],
        'skill_choices': 4,
        'description': 'Un spécialiste des techniques sournoises et des coups précis.'
    },
    'sorcier': {
        'name': 'Sorcier',
        'hit_die': 8,
        'primary_abilities': ['Charisme'],
        'saving_throws': ['Sagesse', 'Charisme'],
        'skills_available': ['Arcanes', 'Tromperie', 'Histoire', 'Intimidation', 'Investigation', 'Nature', 'Religion'],
        'skill_choices': 2,
        'description': 'Un lanceur de sorts qui a conclu un pacte avec un être extraplanaire.'
    }
}

# Compétences disponibles
DND_SKILLS = {
    'acrobaties': 'Acrobaties (Dex)',
    'dressage': 'Dressage (Sag)',
    'arcanes': 'Arcanes (Int)',
    'athlétisme': 'Athlétisme (For)',
    'tromperie': 'Tromperie (Cha)',
    'histoire': 'Histoire (Int)',
    'intuition': 'Intuition (Sag)',
    'intimidation': 'Intimidation (Cha)',
    'investigation': 'Investigation (Int)',
    'médecine': 'Médecine (Sag)',
    'nature': 'Nature (Int)',
    'perception': 'Perception (Sag)',
    'représentation': 'Représentation (Cha)',
    'persuasion': 'Persuasion (Cha)',
    'religion': 'Religion (Int)',
    'escamotage': 'Escamotage (Dex)',
    'discrétion': 'Discrétion (Dex)',
    'survie': 'Survie (Sag)'
}

# Historiques (backgrounds)
DND_BACKGROUNDS = {
    'acolyte': {
        'name': 'Acolyte',
        'skills': ['Intuition', 'Religion'],
        'languages': 2,
        'equipment': 'Symbole sacré, livre de prières, encens',
        'feature': 'Refuge du fidèle'
    },
    'artisan_de_guilde': {
        'name': 'Artisan de guilde',
        'skills': ['Intuition', 'Persuasion'],
        'tools': ['Outils d\'artisan'],
        'languages': 1,
        'equipment': 'Outils d\'artisan, lettre de recommandation de la guilde',
        'feature': 'Membre de guilde'
    },
    'criminel': {
        'name': 'Criminel',
        'skills': ['Tromperie', 'Discrétion'],
        'tools': ['Outils de voleur', 'Jeu'],
        'equipment': 'Pied-de-biche, vêtements sombres avec capuche',
        'feature': 'Contact criminel'
    },
    'erudit': {
        'name': 'Érudit',
        'skills': ['Arcanes', 'Histoire'],
        'languages': 2,
        'equipment': 'Bouteille d\'encre, plume, petit couteau, lettres',
        'feature': 'Chercheur'
    },
    'héros_populaire': {
        'name': 'Héros populaire',
        'skills': ['Dressage', 'Survie'],
        'tools': ['Véhicules terrestres', 'Outils d\'artisan'],
        'equipment': 'Outils d\'artisan, pelle, vêtements de paysan',
        'feature': 'Hospitalité rustique'
    },
    'noble': {
        'name': 'Noble',
        'skills': ['Histoire', 'Persuasion'],
        'tools': ['Jeu'],
        'languages': 1,
        'equipment': 'Vêtements fins, chevalière, parchemin de lignée',
        'feature': 'Position privilégiée'
    },
    'soldat': {
        'name': 'Soldat',
        'skills': ['Athlétisme', 'Intimidation'],
        'tools': ['Véhicules terrestres', 'Jeu'],
        'equipment': 'Insigne de rang, trophée d\'ennemi vaincu',
        'feature': 'Rang militaire'
    }
}