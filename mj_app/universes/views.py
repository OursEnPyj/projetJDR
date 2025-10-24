from django.shortcuts import render, get_object_or_404
from .models import Universe
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
        generated = {
            "name": request.POST.get("name") or f"PNJ-{random.randint(1000,9999)}",
            "class": random.choice(classes),
            "race": random.choice(races),
            "level": random.choice(levels),
            "universe": universe.name,
        }

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
