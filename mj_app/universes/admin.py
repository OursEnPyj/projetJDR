from django.contrib import admin
from .models import Universe

# Register your models here.
@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
    list_display = ("name", "system", "created_at")
    search_fields = ('name', 'system')
