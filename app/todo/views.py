from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Todo

from todo import serializers


class TodoViewSet(viewsets.GenericViewSet, 
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """Manage Todo item in the database"""
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (IsAuthenticated,)
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.order_by('-created_at')

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('created_at')
    
    def perform_create(self, serializer):
        """Create a new Todo"""
        serializer.save(user=self.request.user)