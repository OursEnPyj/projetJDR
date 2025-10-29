from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from universes.models import Universe

def test_universe_debug(request, universe_id):
    """Vue de test pour déboguer le problème."""
    universe = get_object_or_404(Universe, pk=universe_id)
    
    html = f"""
    <h1>Debug Universe {universe_id}</h1>
    <p><strong>Nom:</strong> {universe.name}</p>
    <p><strong>Système:</strong> {universe.system}</p>
    <p><strong>URL pour choose_generation_method:</strong> /characters/generate/{universe_id}/</p>
    <p><strong>Test détection D&D:</strong></p>
    <ul>
        <li>Nom en minuscules: {universe.name.lower()}</li>
        <li>Contient 'donjon': {'donjon' in universe.name.lower()}</li>
        <li>Contient 'd&d': {'d&d' in universe.name.lower()}</li>
        <li>Contient 'dnd': {'dnd' in universe.name.lower()}</li>
        <li>Contient '5e': {'5e' in universe.name.lower()}</li>
    </ul>
    <p><a href="/characters/generate/{universe_id}/">Tester le lien choose_generation_method</a></p>
    <p><a href="/{universe_id}/">Retour à la page univers</a></p>
    """
    
    return HttpResponse(html)