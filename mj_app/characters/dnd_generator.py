import random
import json

# Données pour la génération de personnages D&D 5e en français
DND_RACES = [
    "Humain", "Gnome", "Nain", "Elfe", "Demi-elfe", 
    "Drakéide", "Orc", "Demi-orc", "Halfelin", "Tieffelin"
]

DND_CLASSES = [
    "Barbare", "Barde", "Clerc", "Druide", "Ensorceleur", 
    "Guerrier", "Magicien", "Moine", "Occultiste", "Paladin", 
    "Rôdeur", "Roublard", "Artificier"
]

# Noms par race et genre
RACE_NAMES = {
    "Humain": {
        "masculin": ["Alaric", "Bertrand", "Cédric", "Damien", "Étienne", "Fabien", "Gaston", "Henri", "Julien", "Louis"],
        "féminin": ["Adèle", "Brigitte", "Céline", "Delphine", "Élodie", "Fanny", "Gabrielle", "Hélène", "Isabelle", "Jeanne"]
    },
    "Elfe": {
        "masculin": ["Aelar", "Aramil", "Arannis", "Berrian", "Dayereth", "Enna", "Galinndan", "Heian", "Himo", "Immeral"],
        "féminin": ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Caelynn", "Dara", "Enna", "Galinndan"]
    },
    "Nain": {
        "masculin": ["Adrik", "Baern", "Darrak", "Eberk", "Fargrim", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik"],
        "féminin": ["Amber", "Bardryn", "Diesa", "Eldeth", "Gunnloda", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde"]
    },
    "Gnome": {
        "masculin": ["Alston", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin", "Frug", "Gerrig"],
        "féminin": ["Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick", "Lilli"]
    },
    "Demi-elfe": {
        "masculin": ["Abel", "Caleb", "Corrin", "Dayeth", "Enna", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral"],
        "féminin": ["Adrie", "Althaea", "Caelynn", "Dara", "Enna", "Hadarai", "Immeral", "Ivellios", "Korfel", "Lamlis"]
    },
    "Drakéide": {
        "masculin": ["Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Nadarr", "Pandjed"],
        "féminin": ["Akra", "Biri", "Dare", "Farideh", "Harann", "Havilar", "Jheri", "Kava", "Korinn", "Mishann"]
    },
    "Orc": {
        "masculin": ["Grok", "Thok", "Urok", "Morg", "Grosh", "Durg", "Bagh", "Krusk", "Shump", "Thokk"],
        "féminin": ["Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha", "Sutha"]
    },
    "Demi-orc": {
        "masculin": ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Mhurren", "Ront"],
        "féminin": ["Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha", "Vola"]
    },
    "Halfelin": {
        "masculin": ["Alton", "Ander", "Bernie", "Bobbin", "Cade", "Callus", "Corrin", "Dannad", "Garret", "Lindal"],
        "féminin": ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla"]
    },
    "Tieffelin": {
        "masculin": ["Abad", "Ahvak", "Aramil", "Arannis", "Berrian", "Dayereth", "Enna", "Galinndan", "Heian", "Himo"],
        "féminin": ["Akta", "Anakis", "Armara", "Astaro", "Aym", "Azza", "Beleth", "Bryseis", "Bune", "Criella"]
    }
}

# Descriptions physiques par race
RACE_DESCRIPTIONS = {
    "Humain": {
        "taille": "entre 1m60 et 1m90",
        "poids": "entre 50 et 90 kg",
        "traits": ["cheveux bruns", "cheveux blonds", "cheveux noirs", "cheveux châtains", "yeux bruns", "yeux bleus", "yeux verts", "yeux noisette"],
        "particularités": ["une carrure athlétique", "une silhouette élancée", "des traits fins", "des traits marqués", "une démarche assurée"]
    },
    "Elfe": {
        "taille": "entre 1m50 et 1m80",
        "poids": "entre 40 et 70 kg",
        "traits": ["oreilles pointues", "traits fins et délicats", "cheveux argentés", "cheveux dorés", "yeux améthyste", "yeux émeraude"],
        "particularités": ["une grâce naturelle", "des mouvements fluides", "une aura mystique", "une beauté surnaturelle"]
    },
    "Nain": {
        "taille": "entre 1m20 et 1m50",
        "poids": "entre 60 et 100 kg",
        "traits": ["une barbe fournie", "des traits burinés", "des mains calleuses", "cheveux tressés", "yeux perçants"],
        "particularités": ["une carrure robuste", "une démarche déterminée", "des muscles saillants", "une prestance naturelle"]
    },
    "Gnome": {
        "taille": "entre 90cm et 1m20",
        "poids": "entre 20 et 40 kg",
        "traits": ["un nez proéminent", "des yeux pétillants", "cheveux colorés", "une barbe pointue", "des rides de sourire"],
        "particularités": ["une énergie débordante", "des gestes vifs", "un sourire malicieux", "une curiosité évidente"]
    },
    "Demi-elfe": {
        "taille": "entre 1m55 et 1m85",
        "poids": "entre 45 et 80 kg",
        "traits": ["oreilles légèrement pointues", "traits semi-elfiques", "beauté hybride", "yeux expressifs"],
        "particularités": ["une grâce héritée", "un charisme naturel", "une adaptabilité évidente", "un air pensif"]
    },
    "Drakéide": {
        "taille": "entre 1m70 et 2m00",
        "poids": "entre 70 et 120 kg",
        "traits": ["écailles colorées", "tête draconique", "yeux reptiliens", "griffes acérées", "queue préhensile"],
        "particularités": ["une prestance imposante", "une aura de pouvoir", "des mouvements précis", "une fierté naturelle"]
    },
    "Orc": {
        "taille": "entre 1m70 et 2m10",
        "poids": "entre 80 et 140 kg",
        "traits": ["défenses proéminentes", "peau verdâtre", "yeux rougeoyants", "cicatrices de guerre", "muscles imposants"],
        "particularités": ["une force brute évidente", "une carrure intimidante", "une démarche pesante", "un regard féroce"]
    },
    "Demi-orc": {
        "taille": "entre 1m60 et 2m00",
        "poids": "entre 70 et 120 kg",
        "traits": ["petites défenses", "traits semi-orcs", "peau légèrement verdâtre", "carrure imposante"],
        "particularités": ["une force notable", "un air déterminé", "une rudesse naturelle", "une prestance martiale"]
    },
    "Halfelin": {
        "taille": "entre 80cm et 1m10",
        "poids": "entre 15 et 35 kg",
        "traits": ["pieds poilus", "traits ronds et sympathiques", "cheveux bouclés", "yeux malicieux", "joues rebondies"],
        "particularités": ["une agilité surprenante", "un sourire constant", "une démarche silencieuse", "une bonne humeur contagieuse"]
    },
    "Tieffelin": {
        "taille": "entre 1m50 et 1m80",
        "poids": "entre 50 et 85 kg",
        "traits": ["cornes sur le front", "queue démoniaque", "peau colorée", "yeux sans pupille", "canines acérées"],
        "particularités": ["une aura mystérieuse", "un charisme troublant", "des mouvements gracieux", "une prestance énigmatique"]
    }
}

# Backgrounds génériques
BACKGROUNDS_TEMPLATES = [
    "Né(e) dans {lieu}, {nom} a grandi {enfance}. {événement_marquant} Cette expérience a forgé sa personnalité {trait_personnalité}. Aujourd'hui, {motivation_actuelle}.",
    "{nom} vient d'une famille {origine_famille}. {formation} {événement_important} Désormais, {objectif_personnel}.",
    "L'histoire de {nom} commence à {lieu_origine}. {jeunesse} {tournant} Cette période difficile lui a appris {leçon_apprise}, et maintenant {quête_actuelle}."
]

BACKGROUND_ELEMENTS = {
    "lieu": ["un petit village", "une grande cité", "une ferme isolée", "un monastère", "les rues d'une métropole", "une communauté nomade"],
    "enfance": ["entouré(e) d'une famille aimante", "dans la pauvreté mais avec dignité", "parmi les livres et les érudits", "dans la nature sauvage", "au sein d'une guilde d'artisans"],
    "événement_marquant": ["Un jour, sa famille fut attaquée par des bandits.", "Une catastrophe naturelle détruisit son foyer.", "Il/elle découvrit ses pouvoirs magiques par accident.", "Un mentor mystérieux changea sa vie.", "Une guerre éclata dans sa région."],
    "trait_personnalité": ["déterminée et courageuse", "prudent(e) mais loyal(e)", "curieux/se et téméraire", "sage et réfléchi(e)", "optimiste malgré les épreuves"],
    "motivation_actuelle": ["il/elle voyage pour retrouver sa famille disparue", "il/elle cherche à maîtriser ses pouvoirs", "il/elle veut venger un proche", "il/elle explore le monde par soif de connaissance", "il/elle fuit un passé douloureux"],
    "origine_famille": ["de marchands prospères", "de paysans humbles", "de nobles déchus", "d'aventuriers renommés", "d'artisans respectés"],
    "formation": ["Il/elle a appris les ficelles du commerce.", "Il/elle fut formé(e) aux arts martiaux.", "Il/elle étudia la magie ancienne.", "Il/elle développa ses talents artistiques.", "Il/elle apprit à survivre en nature."],
    "événement_important": ["Mais un scandale ruina sa famille.", "Mais une guerre changea tout.", "Mais il/elle découvrit un secret familial.", "Mais un rival détruisit ses rêves.", "Mais une prophétie bouleversa sa destinée."],
    "objectif_personnel": ["il/elle souhaite restaurer l'honneur familial", "il/elle cherche la vérité sur ses origines", "il/elle veut protéger les innocents", "il/elle poursuit la gloire et la fortune", "il/elle espère trouver sa place dans le monde"],
    "lieu_origine": ["Sombremont", "Val-Doré", "Port-Brume", "Pierrehaute", "Bois-Chantant", "Forge-de-Fer"],
    "jeunesse": ["Il/elle menait une vie paisible.", "Il/elle était connu(e) pour sa bravoure.", "Il/elle passait ses journées à étudier.", "Il/elle aidait sa communauté.", "Il/elle rêvait d'aventure."],
    "tournant": ["Mais un jour, des créatures mystérieuses attaquèrent.", "Mais il/elle fut témoin d'une injustice terrible.", "Mais une vision changea sa perspective.", "Mais il/elle découvrit un artefact ancien.", "Mais un étranger lui révéla sa véritable nature."],
    "leçon_apprise": ["que le courage se trouve dans les moments difficiles", "que la magie peut être dangereuse", "que la justice doit être défendue", "que les apparences sont trompeuses", "que chacun a un destin à accomplir"],
    "quête_actuelle": ["il/elle parcourt le monde en quête de réponses", "il/elle protège ceux qui ne peuvent se défendre", "il/elle cherche à parfaire ses compétences", "il/elle suit les traces d'une légende", "il/elle tente de réparer ses erreurs passées"]
}


def generate_random_character(universe):
    """Génère un personnage D&D 5e complètement aléatoire."""
    
    # Choisir race et classe
    race = random.choice(DND_RACES)
    classe = random.choice(DND_CLASSES)
    
    # Générer le nom
    genre = random.choice(["masculin", "féminin"])
    nom = generate_name(race, genre)
    
    # Générer les caractéristiques (4d6, garder les 3 meilleurs)
    stats = generate_stats()
    
    # Générer la description physique
    description = generate_physical_description(race, genre)
    
    # Générer le background
    background = generate_background(nom, race, classe, genre)
    
    return {
        "name": nom,
        "race": race,
        "char_class": classe,
        "strength": stats["force"],
        "dexterity": stats["dextérité"],
        "constitution": stats["constitution"],
        "intelligence": stats["intelligence"],
        "wisdom": stats["sagesse"],
        "charisma": stats["charisme"],
        "description": description,
        "background": background,
        "universe": universe
    }


def generate_name(race, genre):
    """Génère un nom adapté à la race et au genre."""
    if race in RACE_NAMES and genre in RACE_NAMES[race]:
        return random.choice(RACE_NAMES[race][genre])
    else:
        # Fallback sur les noms humains
        return random.choice(RACE_NAMES["Humain"][genre])


def generate_stats():
    """Génère les caractéristiques avec la méthode 4d6 (garder les 3 meilleurs)."""
    stats = {}
    stat_names = ["force", "dextérité", "constitution", "intelligence", "sagesse", "charisme"]
    
    for stat in stat_names:
        # Lancer 4d6, garder les 3 meilleurs
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.sort(reverse=True)
        stats[stat] = sum(rolls[:3])
    
    return stats


def generate_physical_description(race, genre):
    """Génère une description physique adaptée à la race."""
    if race not in RACE_DESCRIPTIONS:
        race = "Humain"  # Fallback
    
    race_info = RACE_DESCRIPTIONS[race]
    
    # Construire la description
    description_parts = []
    
    # Taille et corpulence
    description_parts.append(f"Mesurant {race_info['taille']}")
    
    # Traits physiques aléatoires
    traits_sélectionnés = random.sample(race_info['traits'], min(2, len(race_info['traits'])))
    if traits_sélectionnés:
        description_parts.append(f"avec {' et '.join(traits_sélectionnés)}")
    
    # Particularité
    particularité = random.choice(race_info['particularités'])
    description_parts.append(f"Il/elle possède {particularité}")
    
    # Trait additionnel aléatoire
    traits_additionnels = [
        "une cicatrice discrète", "un tatouage tribal", "des vêtements simples mais propres",
        "un pendentif précieux", "une démarche confiante", "un regard perçant",
        "des mains expertes", "une voix mélodieuse", "un sourire chaleureux"
    ]
    trait_supplémentaire = random.choice(traits_additionnels)
    description_parts.append(f"On remarque également {trait_supplémentaire}")
    
    return ". ".join(description_parts) + "."


def generate_background(nom, race, classe, genre):
    """Génère un background narratif pour le personnage."""
    template = random.choice(BACKGROUNDS_TEMPLATES)
    
    # Remplir le template avec des éléments aléatoires
    background_vars = {}
    background_vars["nom"] = nom
    
    for key in BACKGROUND_ELEMENTS:
        if f"{{{key}}}" in template:
            background_vars[key] = random.choice(BACKGROUND_ELEMENTS[key])
    
    # Ajuster les pronoms selon le genre
    background_text = template.format(**background_vars)
    
    if genre == "féminin":
        background_text = background_text.replace("Il ", "Elle ")
        background_text = background_text.replace("il ", "elle ")
        background_text = background_text.replace("Né ", "Née ")
        background_text = background_text.replace("né ", "née ")
        background_text = background_text.replace("formé ", "formée ")
        background_text = background_text.replace("connu ", "connue ")
    
    return background_text