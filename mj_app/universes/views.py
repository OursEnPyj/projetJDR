from django.shortcuts import render, get_object_or_404, redirect
from .models import Universe
from characters.models import Character
import random

# Create your views here.
def universe_list(request):
    universes = Universe.objects.all()
    return render(request, "universes/universe_list.html", {"universes": universes})

def universe_detail(request, pk):
    universe = get_object_or_404(Universe, pk=pk)
    return render(request, "universes/universe_detail.html", {"universe": universe})

def generate_character(request, pk):
    universe = get_object_or_404(Universe, pk=pk)
    rules = universe.creation_rules or {}
    # valeurs par défaut si pas de règles définies
    classes = rules.get("classes", ["Adventurer", "Warrior", "Mage"])
    races = rules.get("races", ["Human", "Elf", "Dwarf"])
    levels = rules.get("levels", [1])

    generated = None
    if request.method == "POST":
        action = request.POST.get("action")
        
        if action == "generate":
            generated = {
                "name": request.POST.get("name") or f"PNJ-{random.randint(1000,9999)}",
                "char_class": random.choice(classes),
                "race": random.choice(races),
                "level": random.choice(levels),
                "strength": random.randint(8, 18),
                "dexterity": random.randint(8, 18),
                "constitution": random.randint(8, 18),
                "intelligence": random.randint(8, 18),
                "wisdom": random.randint(8, 18),
                "charisma": random.randint(8, 18),
                "universe": universe.name,
            }
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
                universe=universe,
            )
            return redirect('characters:character_detail', pk=character.pk)

    return render(request, "universes/generate_character.html", {
        "universe": universe,
        "rules": rules,
        "generated": generated,
    })

def universe_monsters(request, pk):
    universe = get_object_or_404(Universe, pk=pk)
    # Placeholder : on propose un lien vers la liste des monstres de l'app monsters filtrée par query param
    # Si vous avez un modèle Monster lié à Universe, vous pouvez charger ici les monstres réels.
    return render(request, "universes/universe_monsters.html", {"universe": universe})
