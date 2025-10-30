from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Character
from .forms import CharacterForm
from universes.models import Universe
from .dnd_generator import generate_random_character


def character_list(request):
    """Affiche la liste de tous les personnages."""
    characters = Character.objects.all()
    # Récupérer le premier univers disponible pour le lien de génération
    first_universe = Universe.objects.first()
    return render(request, 'characters/character_list.html', {
        'characters': characters,
        'first_universe': first_universe
    })


def character_detail(request, pk):
    """Affiche les détails d'un personnage spécifique."""
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'characters/character_detail.html', {'character': character})


def character_update(request, pk):
    """Modifie un personnage existant."""
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            # Sauvegarder les données de base
            character = form.save(commit=False)
            
            # Recalculer les compétences, traits et équipements basés sur la nouvelle race/classe/historique
            if character.race and character.char_class and character.dnd_background:
                from .character_utils import calculate_skills_for_character, get_racial_features
                
                # Préparer le dictionnaire des caractéristiques
                abilities = {
                    'strength': character.strength,
                    'dexterity': character.dexterity,
                    'constitution': character.constitution,
                    'intelligence': character.intelligence,
                    'wisdom': character.wisdom,
                    'charisma': character.charisma
                }
                
                # Calculer les nouvelles compétences
                skills = calculate_skills_for_character(
                    character.race, character.char_class, character.dnd_background, abilities
                )
                character.skills = skills
                
                # Mettre à jour les traits et équipements
                features = get_racial_features(character.race)
                character.features = features
            
            character.save()
            return redirect('characters:character_detail', pk=character.pk)
    else:
        form = CharacterForm(instance=character)
    
    return render(request, 'characters/characters_form.html', {'form': form, 'character': character})


def character_delete(request, pk):
    """Supprime un personnage."""
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        character.delete()
        return redirect('characters:character_list')
    return render(request, 'characters/character_confirm_delete.html', {'character': character})


def choose_universe_for_generation(request):
    """Permet de choisir un univers pour générer un personnage."""
    universes = Universe.objects.all()
    return render(request, 'characters/choose_universe.html', {'universes': universes})


def choose_generation_method(request, universe_id):
    """Permet de choisir la méthode de génération pour un univers spécifique."""
    universe = get_object_or_404(Universe, pk=universe_id)
    
    # Vérifier si c'est l'univers D&D 5e (détection plus flexible)
    universe_name_lower = universe.name.lower()
    is_dnd_5e = (
        ("donjon" in universe_name_lower or "d&d" in universe_name_lower or "dnd" in universe_name_lower) and 
        "5e" in universe_name_lower
    )
    
    # Debug: afficher des infos dans la console
    print(f"DEBUG: Universe name: '{universe.name}'")
    print(f"DEBUG: Universe name lower: '{universe_name_lower}'")
    print(f"DEBUG: Is D&D 5e: {is_dnd_5e}")
    
    # TEMPORAIRE: Toujours afficher la page de sélection pour déboguer
    return render(request, 'characters/choose_generation_method_dnd.html', {
        'universe': universe
    })


def dnd_random_generation(request, universe_id):
    """Génération complètement aléatoire pour D&D 5e."""
    universe = get_object_or_404(Universe, pk=universe_id)
    
    generated = None
    if request.method == "POST":
        action = request.POST.get("action")
        
        if action == "generate":
            # Générer un nouveau personnage aléatoire
            generated = generate_random_character(universe)
        elif action == "save":
            # Sauvegarder le personnage généré
            character = Character.objects.create(
                name=request.POST.get("character_name"),
                race=request.POST.get("character_race"),
                char_class=request.POST.get("character_class"),
                strength=int(request.POST.get("character_strength", 10)),
                dexterity=int(request.POST.get("character_dexterity", 10)),
                constitution=int(request.POST.get("character_constitution", 10)),
                intelligence=int(request.POST.get("character_intelligence", 10)),
                wisdom=int(request.POST.get("character_wisdom", 10)),
                charisma=int(request.POST.get("character_charisma", 10)),
                description=request.POST.get("character_description", ""),
                background_story=request.POST.get("character_background", ""),
                dnd_background=request.POST.get("character_dnd_background", ""),
                universe=universe,
            )
            return redirect('characters:character_detail', pk=character.pk)
    
    return render(request, 'characters/dnd_random_generation.html', {
        'universe': universe,
        'method_name': 'Génération Aléatoire',
        'generated': generated
    })


def dnd_manual_creation(request, universe_id):
    """Création manuelle pour D&D 5e avec interface multi-étapes."""
    from .dnd_data import DND_RACES, DND_CLASSES, DND_SKILLS, DND_BACKGROUNDS
    from .character_utils import (
        calculate_skills_for_character, 
        get_racial_features, 
        get_class_features, 
        get_background_features,
        get_starting_equipment,
        apply_racial_bonuses
    )
    
    universe = get_object_or_404(Universe, pk=universe_id)
    
    if request.method == 'POST':
        # Traitement de la soumission du formulaire
        if 'save_character' in request.POST:
            # Récupérer les données du formulaire
            race_name = request.POST.get('race', '')
            class_name = request.POST.get('character_class', '')
            background_name = request.POST.get('background', '')
            background_story = request.POST.get('background_story', '')
            
            # Trouver les clés correspondantes
            race_key = None
            class_key = None
            background_key = None
            
            for key, data in DND_RACES.items():
                if data['name'] == race_name:
                    race_key = key
                    break
                    
            for key, data in DND_CLASSES.items():
                if data['name'] == class_name:
                    class_key = key
                    break
                    
            for key, data in DND_BACKGROUNDS.items():
                if data['name'] == background_name:
                    background_key = key
                    break
            
            # Caractéristiques de base
            base_abilities = {
                'strength': int(request.POST.get('strength', 10)),
                'dexterity': int(request.POST.get('dexterity', 10)),
                'constitution': int(request.POST.get('constitution', 10)),
                'intelligence': int(request.POST.get('intelligence', 10)),
                'wisdom': int(request.POST.get('wisdom', 10)),
                'charisma': int(request.POST.get('charisma', 10)),
            }
            
            # Appliquer les bonus raciaux
            final_abilities = apply_racial_bonuses(base_abilities.copy(), race_key)
            
            # Calculer compétences, traits et équipement
            skills = calculate_skills_for_character(race_key, class_key, background_key, final_abilities)
            
            features = []
            features.extend(get_racial_features(race_key))
            features.extend(get_class_features(class_key))
            features.extend(get_background_features(background_key))
            
            equipment = get_starting_equipment(class_name, background_name)
            
            # Langues (récupérées des données raciales)
            languages = []
            if race_key and race_key in DND_RACES:
                languages = DND_RACES[race_key].get('languages', [])
            
            # Créer le personnage avec toutes les données
            character_data = {
                'name': request.POST.get('name', ''),
                'race': race_name,
                'char_class': class_name,
                'level': 1,
                'strength': final_abilities['strength'],
                'dexterity': final_abilities['dexterity'],
                'constitution': final_abilities['constitution'],
                'intelligence': final_abilities['intelligence'],
                'wisdom': final_abilities['wisdom'],
                'charisma': final_abilities['charisma'],
                'dnd_background': background_name,
                'background_story': background_story,
                'description': request.POST.get('description', ''),
                'skills': skills,
                'equipment': equipment,
                'features': features,
                'languages': languages,
                'universe': universe
            }
            
            character = Character.objects.create(**character_data)
            return redirect('characters:character_detail', pk=character.pk)
    
    # Calculer les modificateurs pour affichage
    def get_modifier(score):
        return (score - 10) // 2
    
    context = {
        'universe': universe,
        'method_name': 'Création Manuelle',
        'races': DND_RACES,
        'classes': DND_CLASSES,
        'skills': DND_SKILLS,
        'backgrounds': DND_BACKGROUNDS,
        'get_modifier': get_modifier,
    }
    
    return render(request, 'characters/dnd_manual_creation.html', context)


    def get_modifier(score):
        return (score - 10) // 2
