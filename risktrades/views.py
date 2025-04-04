from rest_framework import viewsets
from .models import RiskTrade
from .serializers import RiskTradeSerializer

class RiskTradeViewSet(viewsets.ModelViewSet):
    queryset = RiskTrade.objects.all()
    serializer_class = RiskTradeSerializer

  