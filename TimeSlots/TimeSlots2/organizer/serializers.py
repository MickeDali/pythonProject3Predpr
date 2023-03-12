from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers, HyperLinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description']
