from rest_framework import serializers
from .models import RiskTrade

class RiskTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTrade
        fields = '__all__'  # Include all fields in the model
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')  # Make these fields read-only

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user  # Automatically assigns the logged-in user
        return super().create(validated_data)

         