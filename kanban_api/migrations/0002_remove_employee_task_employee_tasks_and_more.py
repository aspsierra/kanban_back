# Generated by Django 5.1.3 on 2024-12-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='task',
        ),
        migrations.AddField(
            model_name='employee',
            name='tasks',
            field=models.ManyToManyField(blank=True, related_name='employees', to='kanban_api.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
