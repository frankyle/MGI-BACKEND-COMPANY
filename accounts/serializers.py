from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import UserAccount

class UserAccountSerializer(UserSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'nationality')

class UserAccountCreateSerializer(UserCreateSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'nationality')
