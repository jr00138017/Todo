from rest_framework import serializers
from todolist.models import Todo


class TodolistSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'datecompleted', 'important']


class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        read_only_fields = ['title', 'memo', 'created', 'datecompleted', 'important']
        fields = ['id']
