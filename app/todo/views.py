from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Todo

from todo import serializers


class TodoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage Todo in the database"""
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (IsAuthenticated,)
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.order_by('-created_at')