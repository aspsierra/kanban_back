from rest_framework import serializers
from .models import Kanban, Task, Employee

class KanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = ['id', 'title']