from rest_framework import serializers
from todolist.models import Todo


class TodolistSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()


    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'datecompleted', 'important']
