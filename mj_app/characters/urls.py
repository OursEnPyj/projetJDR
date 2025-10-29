from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('new/', views.character_create, name='character_create'),
    path('generate/', views.choose_universe_for_generation, name='choose_universe_for_generation'),
    path('generate/<int:universe_id>/', views.choose_generation_method, name='choose_generation_method'),
    
    # Méthodes de génération D&D 5e
    path('generate/<int:universe_id>/random/', views.dnd_random_generation, name='dnd_random_generation'),
    path('generate/<int:universe_id>/manual/', views.dnd_manual_creation, name='dnd_manual_creation'),
    path('generate/<int:universe_id>/pointbuy/', views.dnd_point_buy_system, name='dnd_point_buy_system'),
    path('generate/<int:universe_id>/balanced/', views.dnd_balanced_generation, name='dnd_balanced_generation'),
    
    path('<int:pk>/', views.character_detail, name='character_detail'),
    path('<int:pk>/edit/', views.character_update, name='character_update'),
    path('<int:pk>/delete/', views.character_delete, name='character_delete'),
]
