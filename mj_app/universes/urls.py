from django.urls import path
from . import views

app_name = 'universes'

urlpatterns = [
    # liste des univers (existante)
    path("", views.universe_list, name="universe_list"),
    # page détail + outils pour un univers donné
    path("<int:pk>/", views.universe_detail, name="universe_detail"),
    # générateur de personnage pour un univers
    path("<int:pk>/generate-character/", views.generate_character, name="generate_character"),
    # liste / générateur de monstres lié à l'univers (placeholder)
    path("<int:pk>/monsters/", views.universe_monsters, name="universe_monsters"),
]
