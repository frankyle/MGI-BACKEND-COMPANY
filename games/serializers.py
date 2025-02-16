from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'  # Include all fields, or specify the fields you need
        read_only_fields = ('user', 'created_at', 'updated_at') 
