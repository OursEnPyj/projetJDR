from django.contrib import admin
from .models import Character

# Register your models here.

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'universe', 'owner', 'created_at')
    list_filter = ('universe',)
    search_fields = ('name', 'owner__username')
