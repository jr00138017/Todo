from rest_framework import generics, permissions
from .serializers import TodolistSerializer
from todolist.models import Todo


class TodoCompleted(generics.ListAPIView):
    serializer_class = TodolistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')
