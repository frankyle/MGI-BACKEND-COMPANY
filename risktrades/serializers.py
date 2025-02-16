from rest_framework import serializers
from .models import RiskTrade

class RiskTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTrade
        fields = '__all__'  # Include all fields in the model
        read_only_fields = ('user', 'created_at', 'updated_at')  # Make these fields read-only
