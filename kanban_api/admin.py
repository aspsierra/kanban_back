from django.contrib import admin
from . import models


class KanbanAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']

class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'kanban', 'employee_list']
    list_filter = ['kanban', 'employees']

    def employee_list(self, obj):
        return ', '.join([employee.name for employee in obj.employees.all()]) 

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'task_list']
    list_filter = ['tasks']

    def task_list(self, obj):
        return ', '.join([task.title for task in obj.tasks.all()]) 


admin.site.register(models.Kanban, KanbanAdmin)
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Employee, EmployeeAdmin)



