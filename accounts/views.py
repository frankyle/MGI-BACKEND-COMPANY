from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .models import UserAccount
from .serializers import UserAccountSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    pass  # Customize if needed

class UserListView(generics.ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    lookup_field = 'id'
