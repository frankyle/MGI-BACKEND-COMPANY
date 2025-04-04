from rest_framework import serializers
from .models import Toy

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'  # Includes all fields
        read_only_fields = ['id', 'user']  # Prevents modification of these fields

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user  # Automatically assigns the logged-in user
        return super().create(validated_data)
 