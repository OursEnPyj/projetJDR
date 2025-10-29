from django.urls import path
from . import views

app_name = 'monsters'

urlpatterns = [
    path('', views.monster_list, name='monster_list'),
    path('generate/', views.monster_generator, name='monster_generator'),
]