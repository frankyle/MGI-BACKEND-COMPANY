from rest_framework import viewsets
from .models import CandleImages
from .serializers import CandleImagesSerializer
from rest_framework.permissions import IsAuthenticated

class CandleImagesViewSet(viewsets.ModelViewSet):
    queryset = CandleImages.objects.all()
    serializer_class = CandleImagesSerializer
    permission_classes = [IsAuthenticated]