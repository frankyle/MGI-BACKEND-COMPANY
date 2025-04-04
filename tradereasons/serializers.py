from rest_framework import serializers
from .models import TradeReasons

class TradeReasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeReasons
        fields = '__all__'
