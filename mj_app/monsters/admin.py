from django.contrib import admin
from .models import Monster

# Register your models here.

@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'hit_points', 'armor_class')
    search_fields = ('name', 'type')