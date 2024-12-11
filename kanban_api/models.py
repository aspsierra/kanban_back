from django.db import models

class Kanban(models.Model):
    title = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    kanban = models.ForeignKey(Kanban, on_delete=models.CASCADE, related_name='tasks', blank=False, null=False)

    def __str__(self):
        return f'{self.title} ({self.kanban})'

class Employee(models.Model):
    name = models.CharField(max_length=50, null=False)
    tasks = models.ManyToManyField(Task, related_name='employees', blank=True)

    def __str__(self):
        return self.name