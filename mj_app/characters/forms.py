from django import forms
from .models import Character
from universes.models import Universe


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
            "race": forms.TextInput(attrs={"class": "form-control", "placeholder": "ex: Humain, Elfe, Nain"}),
            "char_class": forms.TextInput(attrs={"class": "form-control", "placeholder": "ex: Guerrier, Mage, Voleur"}),
            "level": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20"}),
            "strength": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20"}),
            "dexterity": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20"}),
            "constitution": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20"}),
            "intelligence": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20"}),
            "wisdom": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20"}),
            "charisma": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20"}),
            "dnd_background": forms.TextInput(attrs={"class": "form-control", "placeholder": "ex: Noble, Criminel, Érudit"}),
            "background_story": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Histoire personnelle du personnage"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Description physique du personnage"}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personnaliser l'affichage du champ universe
        self.fields['universe'].queryset = Universe.objects.all()
        self.fields['universe'].empty_label = "Sélectionnez un univers"
