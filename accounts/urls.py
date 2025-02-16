from django.urls import path, include
from .views import CustomTokenObtainPairView, UserListView, UserDetailView

urlpatterns = [
    path('', include('djoser.urls')),  # Include Djoser endpoints
    path('', include('djoser.urls.jwt')),  # JWT endpoints for authentication
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
]
