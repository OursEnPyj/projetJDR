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


def character_create(request):
    """Crée un nouveau personnage."""
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save()
            return redirect('characters:character_detail', pk=character.pk)
    else:
        form = CharacterForm()
    return render(request, 'characters/characters_form.html', {'form': form})


def character_update(request, pk):
    """Modifie un personnage existant."""
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
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
                background=request.POST.get("character_background", ""),
                universe=universe,
            )
            return redirect('characters:character_detail', pk=character.pk)
    
    return render(request, 'characters/dnd_random_generation.html', {
        'universe': universe,
        'method_name': 'Génération Aléatoire',
        'generated': generated
    })


def dnd_manual_creation(request, universe_id):
    """Création manuelle pour D&D 5e."""
    universe = get_object_or_404(Universe, pk=universe_id)
    return render(request, 'characters/dnd_manual_creation.html', {
        'universe': universe,
        'method_name': 'Création Manuelle'
    })


def dnd_point_buy_system(request, universe_id):
    """Système de points (27 points) pour D&D 5e."""
    universe = get_object_or_404(Universe, pk=universe_id)
    return render(request, 'characters/dnd_point_buy_system.html', {
        'universe': universe,
        'method_name': 'Système à 27 Points'
    })


def dnd_balanced_generation(request, universe_id):
    """Génération équilibrée race/classe pour D&D 5e."""
    universe = get_object_or_404(Universe, pk=universe_id)
    return render(request, 'characters/dnd_balanced_generation.html', {
        'universe': universe,
        'method_name': 'Génération Équilibrée'
    })
