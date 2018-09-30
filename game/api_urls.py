from django.urls import path, include
from .api_views import search_battle, battle_wait, battle_view

urlpatterns = [
    path('search-battle/', search_battle, name='search-battle'),
    path('pull/', battle_wait, name='pull-battle'),
    path('battle/<int:id>/', battle_view, name='battle'),
    path('battle/<int:id>/pull/', battle_view, name='battle-pull')
]
