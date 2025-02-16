from rest_framework import viewsets
from .models import Toy
from .serializers import ToySerializer

class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
