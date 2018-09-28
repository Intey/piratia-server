from django.urls import path, include
from .api_views import token

urlpatterns = [
    path('token/', token, name='token'),
]
