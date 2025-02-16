from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()  # Retrieve all game records
    serializer_class = GameSerializer  # Use the GameSerializer for the response

    def perform_create(self, serializer):
        # Set the user to the current logged-in user
        serializer.save(user=self.request.user)
