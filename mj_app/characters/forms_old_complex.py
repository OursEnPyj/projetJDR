from django import forms
from .models import Character
from universes.models import Universe

# Choix statiques pour les dropdowns D&D
RACE_CHOICES = [
    ('', 'Sélectionnez une race'),
    ('humain', 'Humain'),
    ('elfe', 'Elfe'),
    ('nain', 'Nain'),
    ('halfelin', 'Halfelin'),
    ('drakéide', 'Drakéide'),
    ('gnome', 'Gnome'),
    ('demi-elfe', 'Demi-elfe'),
    ('demi-orc', 'Demi-orc'),
    ('tieffelin', 'Tieffelin'),
]

CLASS_CHOICES = [
    ('', 'Sélectionnez une classe'),
    ('barbare', 'Barbare'),
    ('barde', 'Barde'),
    ('clerc', 'Clerc'),
    ('druide', 'Druide'),
    ('ensorceleur', 'Ensorceleur'),
    ('guerrier', 'Guerrier'),
    ('magicien', 'Magicien'),
    ('moine', 'Moine'),
    ('paladin', 'Paladin'),
    ('rôdeur', 'Rôdeur'),
    ('roublard', 'Roublard'),
    ('sorcier', 'Sorcier'),
]

BACKGROUND_CHOICES = [
    ('', 'Sélectionnez un historique'),
    ('acolyte', 'Acolyte'),
    ('artisan_de_guilde', 'Artisan de guilde'),
    ('criminel', 'Criminel'),
    ('erudit', 'Érudit'),
    ('héros_populaire', 'Héros populaire'),
    ('noble', 'Noble'),
    ('soldat', 'Soldat'),
]


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
            "race": forms.Select(choices=RACE_CHOICES, attrs={"class": "form-control", "id": "id_race"}),
            "char_class": forms.Select(choices=CLASS_CHOICES, attrs={"class": "form-control", "id": "id_char_class"}),
            "level": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20"}),
            "strength": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_strength"}),
            "dexterity": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_dexterity"}),
            "constitution": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_constitution"}),
            "intelligence": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_intelligence"}),
            "wisdom": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_wisdom"}),
            "charisma": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "20", "id": "id_charisma"}),
            "dnd_background": forms.Select(choices=BACKGROUND_CHOICES, attrs={"class": "form-control", "id": "id_dnd_background"}),
            "background_story": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Histoire personnelle du personnage"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Description physique du personnage"}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personnaliser l'affichage du champ universe
        self.fields['universe'].queryset = Universe.objects.all()
        self.fields['universe'].empty_label = "Sélectionnez un univers"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personnaliser l'affichage du champ universe
        self.fields['universe'].queryset = Universe.objects.all()
        self.fields['universe'].empty_label = "Sélectionnez un univers"
        
        # Définir les choix pour les champs D&D dynamiquement
        self.fields['race'].choices = get_race_choices()
        self.fields['char_class'].choices = get_class_choices()
        self.fields['dnd_background'].choices = get_background_choices()
        
        # Gérer la correspondance des anciennes valeurs avec les nouvelles clés
        if self.instance and self.instance.pk:
            # Convertir les anciennes valeurs vers les nouvelles clés si nécessaire
            if self.instance.race in RACE_MAPPING:
                self.instance.race = RACE_MAPPING[self.instance.race]
            if self.instance.char_class in CLASS_MAPPING:
                self.instance.char_class = CLASS_MAPPING[self.instance.char_class]
            if self.instance.dnd_background in BACKGROUND_MAPPING:
                self.instance.dnd_background = BACKGROUND_MAPPING[self.instance.dnd_background]
    
    def save(self, commit=True):
        # S'assurer que les valeurs sauvegardées utilisent les nouvelles clés
        instance = super().save(commit=False)
        
        # Pas besoin de conversion supplémentaire car les choix du formulaire utilisent déjà les bonnes clés
        if commit:
            instance.save()
        return instance