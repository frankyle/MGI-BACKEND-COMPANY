from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import RiskTrade
from .serializers import RiskTradeSerializer

class RiskTradeViewSet(viewsets.ModelViewSet):
    queryset = RiskTrade.objects.all()
    serializer_class = RiskTradeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure only risk trades for the logged-in user are returned
        return RiskTrade.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save the user who creates the risk trade
        serializer.save(user=self.request.user)
