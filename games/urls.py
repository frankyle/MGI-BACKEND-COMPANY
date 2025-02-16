from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)  # Register the GameViewSet with the URL path 'games'

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]
