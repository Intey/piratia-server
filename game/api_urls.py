from django.urls import path, include
from .api_views import data_view

urlpatterns = [
    path('search-battle/', data_view, name='search-battle'),
]
