from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            "name",
            "race",
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
            "description",
            "background",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "background": forms.Textarea(attrs={"rows": 5}),
        }
