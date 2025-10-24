from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('new/', views.character_create, name='character_create'),
    path('<int:pk>/', views.character_detail, name='character_detail'),
    path('<int:pk>/edit/', views.character_update, name='character_update'),
    path('<int:pk>/delete/', views.character_delete, name='character_delete'),
]
