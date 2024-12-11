from rest_framework import serializers
from .models import Kanban, Task, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name']

class TaskSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True)
    class Meta:
        model = Task
        fields = ['title', 'description', 'employees']

class KanbanSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = Kanban
        fields = ['id', 'title', 'tasks']