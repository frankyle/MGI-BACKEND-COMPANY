from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TradeReasonsViewSet  # Import your viewset

router = DefaultRouter()
router.register(r'tradereasons', TradeReasonsViewSet, basename='tradereason')  # Use a basename for consistency

urlpatterns = [
    path('', include(router.urls)),  # No additional path here
]

