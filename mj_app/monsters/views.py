from django.shortcuts import render
from .models import Monster
from .utils import generate_monster

# Create your views here.

def monster_list(request):
    monsters = Monster.objects.all()
    return render(request, 'monsters/monster_list.html', {'monsters': monsters})

def monster_generator(request):
    monster = None
    if request.method == 'POST':
        monster = generate_monster()
    return render(request, 'monsters/monster_generator.html', {'monster': monster})