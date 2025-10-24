from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Character
from .forms import CharacterForm


def character_list(request):
    """Affiche la liste de tous les personnages."""
    characters = Character.objects.all()
    return render(request, 'characters/character_list.html', {'characters': characters})


def character_detail(request, pk):
    """Affiche les détails d'un personnage spécifique."""
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'characters/character_detail.html', {'character': character})


def character_create(request):
    """Crée un nouveau personnage."""
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('character_list')
    else:
        form = CharacterForm()
    return render(request, 'characters/character_form.html', {'form': form})


def character_update(request, pk):
    """Modifie un personnage existant."""
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm(instance=character)
    return render(request, 'characters/character_form.html', {'form': form, 'character': character})


def character_delete(request, pk):
    """Supprime un personnage."""
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        character.delete()
        return redirect('character_list')
    return render(request, 'characters/character_confirm_delete.html', {'character': character})
