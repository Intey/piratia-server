from django.urls import path, include
from .api_views import search_battle, wait_for_battle, battle_view

urlpatterns = [
    path('search-battle/', search_battle, name='search-battle'),
    path('pull/', wait_for_battle, name='wait-for-battle'),
    path('battle/<int:id>/', battle_view, name='battle'),
    path('battle/<int:id>/battle-wait/', battle_view, name='battle-pull')
]
