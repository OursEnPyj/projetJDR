from django import forms
from .models import Character
from universes.models import Universe
from .dnd_data import DND_RACES, DND_CLASSES, DND_BACKGROUNDS

# Générer les choix dynamiquement depuis dnd_data.py
def get_race_choices():
    choices = [('', 'Sélectionnez une race')]
    for key, race_data in DND_RACES.items():
        choices.append((key, race_data['name']))
    return choices

def get_class_choices():
    choices = [('', 'Sélectionnez une classe')]
    for key, class_data in DND_CLASSES.items():
        choices.append((key, class_data['name']))
    return choices

def get_background_choices():
    choices = [('', 'Sélectionnez un historique')]
    for key, bg_data in DND_BACKGROUNDS.items():
        choices.append((key, bg_data['name']))
    return choices


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            "name",
            "universe",
            "race",
            "char_class",
            "level",
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
            "dnd_background",
            "background_story",
            "description",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nom du personnage"}),
            "universe": forms.Select(attrs={"class": "form-control"}),
            "race": forms.Select(attrs={"class": "form-control", "id": "id_race"}),
            "char_class": forms.Select(attrs={"class": "form-control", "id": "id_char_class"}),
            "level": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20"}),
            "strength": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_strength"}),
            "dexterity": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_dexterity"}),
            "constitution": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_constitution"}),
            "intelligence": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_intelligence"}),
            "wisdom": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_wisdom"}),
            "charisma": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_charisma"}),
            "dnd_background": forms.Select(attrs={"class": "form-control", "id": "id_dnd_background"}),
            "background_story": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Histoire personnelle du personnage"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Description physique du personnage"}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personnaliser l'affichage du champ universe
        self.fields['universe'].queryset = Universe.objects.all()
        self.fields['universe'].empty_label = "Sélectionnez un univers"
        
        # Définir les choix pour les champs D&D dynamiquement
        self.fields['race'].choices = get_race_choices()
        self.fields['char_class'].choices = get_class_choices()
        self.fields['dnd_background'].choices = get_background_choices()
