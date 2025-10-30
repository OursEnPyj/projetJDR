from django import forms
from .models import Character
from universes.models import Universe
import json

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
            "skills",
            "equipment",
            "features",
            "languages",
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
            "skills": forms.Textarea(attrs={"class": "form-control", "rows": 8, "placeholder": "Compétences du personnage (une par ligne)\nExemple:\nAcrobaties (Dex): +5 (Maîtrise)\nAthlétisme (For): +3 (Normal)\nDiscrétion (Dex): +8 (Expert)"}),
            "equipment": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Équipement (format JSON ou liste)"}),
            "features": forms.Textarea(attrs={"class": "form-control", "rows": 8, "placeholder": "Traits et capacités (format JSON ou texte libre)"}),
            "languages": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Langues parlées (format JSON ou liste)"}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personnaliser l'affichage du champ universe
        self.fields['universe'].queryset = Universe.objects.all()
        self.fields['universe'].empty_label = "Sélectionnez un univers"
        
        # Préparer les champs JSON pour l'affichage
        if self.instance and self.instance.pk:
            self._prepare_json_fields()
    
    def _prepare_json_fields(self):
        """Prépare l'affichage des champs JSON pour le formulaire."""
        # Skills
        if self.instance.skills:
            self.initial['skills'] = self._format_skills_display(self.instance.skills)
        
        # Equipment
        if self.instance.equipment:
            self.initial['equipment'] = self._format_list_display(self.instance.equipment)
        
        # Features
        if self.instance.features:
            self.initial['features'] = self._format_features_display(self.instance.features)
        
        # Languages
        if self.instance.languages:
            self.initial['languages'] = self._format_list_display(self.instance.languages)
    
    def _format_skills_display(self, skills):
        """Formate les compétences pour l'affichage dans le formulaire."""
        if isinstance(skills, dict):
            lines = []
            for skill_key, skill_data in skills.items():
                if isinstance(skill_data, dict):
                    # Nouveau format simplifié avec le nom complet de la compétence
                    skill_name = skill_data.get('name', skill_key)
                    bonus = skill_data.get('bonus', 0)
                    proficient = skill_data.get('proficient', False)
                    expert = skill_data.get('expert', False)
                    
                    # Format simple : Nom: +bonus (statut)
                    status = "Expert" if expert else "Maîtrise" if proficient else "Normal"
                    lines.append(f"{skill_name}: +{bonus} ({status})")
                else:
                    # Ancien format simple
                    lines.append(f"{skill_key}: +{skill_data}")
            return "\n".join(lines)
        return str(skills)
    
    def _format_features_display(self, features):
        """Formate les capacités pour l'affichage dans le formulaire."""
        if isinstance(features, list):
            lines = []
            for feature in features:
                if isinstance(feature, dict):
                    name = feature.get('name', 'Capacité inconnue')
                    description = feature.get('description', '')
                    source = feature.get('source', '')
                    line = f"• {name}"
                    if source:
                        line += f" ({source})"
                    if description:
                        line += f": {description}"
                    lines.append(line)
                else:
                    lines.append(f"• {feature}")
            return "\n".join(lines)
        return str(features)
    
    def _format_list_display(self, items):
        """Formate une liste pour l'affichage dans le formulaire."""
        if isinstance(items, list):
            return "\n".join([f"• {item}" for item in items])
        return str(items)
    
    def clean_skills(self):
        """Valide et nettoie le champ skills."""
        skills_data = self.cleaned_data.get('skills', '')
        if not skills_data:
            return {}
        
        # Si c'est déjà du JSON valide, on le garde
        if isinstance(skills_data, dict):
            return skills_data
        
        # Sinon, on essaie de parser du texte
        return self._parse_skills_text(skills_data)
    
    def clean_equipment(self):
        """Valide et nettoie le champ equipment."""
        equipment_data = self.cleaned_data.get('equipment', '')
        if not equipment_data:
            return []
        
        if isinstance(equipment_data, list):
            return equipment_data
        
        return self._parse_list_text(equipment_data)
    
    def clean_features(self):
        """Valide et nettoie le champ features."""
        features_data = self.cleaned_data.get('features', '')
        if not features_data:
            return []
        
        if isinstance(features_data, list):
            return features_data
        
        return self._parse_features_text(features_data)
    
    def clean_languages(self):
        """Valide et nettoie le champ languages."""
        languages_data = self.cleaned_data.get('languages', '')
        if not languages_data:
            return []
        
        if isinstance(languages_data, list):
            return languages_data
        
        return self._parse_list_text(languages_data)
    
    def _parse_skills_text(self, text):
        """Parse le texte des compétences."""
        skills = {}
        for line in text.strip().split('\n'):
            line = line.strip()
            if ':' in line:
                parts = line.split(':', 1)
                skill_name = parts[0].strip()
                skill_info = parts[1].strip()
                
                # Créer une clé simple à partir du nom complet
                # Ex: "Acrobaties (Dex)" -> "acrobaties"
                skill_key = skill_name.split('(')[0].strip().lower()
                
                # Essayer de parser le bonus
                bonus = 0
                proficient = False
                expert = False
                
                try:
                    if '+' in skill_info:
                        bonus_str = skill_info.split('(')[0].strip()
                        bonus = int(bonus_str.replace('+', ''))
                        
                        # Vérifier la maîtrise
                        proficient = 'Maîtrise' in skill_info or 'Expert' in skill_info
                        expert = 'Expert' in skill_info
                        
                except:
                    pass
                
                skills[skill_key] = {
                    'name': skill_name,
                    'bonus': bonus,
                    'proficient': proficient,
                    'expert': expert
                }
        
        return skills
    
    def _parse_features_text(self, text):
        """Parse le texte des capacités."""
        features = []
        for line in text.strip().split('\n'):
            line = line.strip()
            if line and line.startswith('•'):
                line = line[1:].strip()
            
            if ':' in line:
                parts = line.split(':', 1)
                name = parts[0].strip()
                description = parts[1].strip()
                
                # Vérifier s'il y a une source entre parenthèses dans le nom
                source = ''
                if '(' in name and ')' in name:
                    source_match = name[name.rfind('('):name.rfind(')')+1]
                    if source_match:
                        source = source_match[1:-1]  # Enlever les parenthèses
                        name = name.replace(source_match, '').strip()
                
                features.append({
                    'name': name,
                    'description': description,
                    'source': source
                })
            elif line:
                features.append({'name': line, 'description': '', 'source': ''})
        
        return features
    
    def _parse_list_text(self, text):
        """Parse une liste textuelle."""
        items = []
        for line in text.strip().split('\n'):
            line = line.strip()
            if line:
                if line.startswith('•'):
                    line = line[1:].strip()
                items.append(line)
        
        return items