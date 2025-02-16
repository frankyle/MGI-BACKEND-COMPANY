from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RiskTradeViewSet

router = DefaultRouter()
router.register(r'risktrades', RiskTradeViewSet, basename='risktrade')

urlpatterns = [
    path('', include(router.urls)),
]
