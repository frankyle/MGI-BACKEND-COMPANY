from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import TradeReasons
from .serializers import TradeReasonsSerializer
from rest_framework.permissions import IsAuthenticated

class TradeReasonsViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing TradeReasons. Provides full CRUD functionality.
    """
    queryset = TradeReasons.objects.all()
    serializer_class = TradeReasonsSerializer
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access

    def create(self, request, *args, **kwargs):
        """
        Overriding the create method to automatically associate the authenticated user.
        """
        # Add the user ID to the request data
        request.data['user'] = request.user.id

        # Serialize the incoming data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Automatically handles validation errors

        # Save the object and return the response
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        """
        Perform the creation of a new TradeReasons object.
        This allows additional customization if needed.
        """
        serializer.save()

    def update(self, request, *args, **kwargs):
        """
        Overriding the update method to include additional logic if needed.
        """
        print(request.data)  # Debug incoming data
        partial = kwargs.pop('partial', False)  # Supports both PUT and PATCH
        instance = self.get_object()

        # Update the instance with new data
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Save the changes and return the response
        self.perform_update(serializer)
        
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Overriding the destroy method to add additional cleanup logic if needed.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
